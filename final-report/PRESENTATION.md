# AC5211 · Báo cáo cuối kỳ: LoRA + SDM cho Text-Based Person Search

**Đỗ Thanh Tùng · 20252432M** · AC5211 Multimedia Database

Tài liệu này dùng để chuẩn bị thuyết trình. Nó giải thích chi tiết hơn báo cáo IEEE 6 trang (`main.pdf`) ở ba điểm: các kết quả, key insight, và lý do SDM tốt hơn (kể cả trong FedAvg). Số liệu của 3 run loss lấy từ `generated/numbers.tex` và `generated/curve_*.csv`. Số liệu FedAvg ở mục 9.2 lấy từ log của các run FedAvg sơ bộ; phần này **không có trong báo cáo PDF**, chỉ dùng khi bị hỏi thêm.

---

## 0. Ba thông điệp chính

1. **PEFT đủ dùng.** Chỉ train 0.49M tham số (0.33%, ít hơn 304 lần so với full fine-tune), LoRA + SDM vẫn đạt **58.85% R@1 ở peak** và **57.18% khi hội tụ**. Con số này ngang với **57.20%** của IRRA khi full fine-tune với SDM. Đây là tiền đề để dùng LoRA trong FL: mỗi client upload 1.88 MiB mỗi round thay vì 571 MiB.
2. **SDM thắng InfoNCE nhưng không vì lý do IRRA đưa ra.** Với random sampling, chỉ **1.52%** số dòng trong batch có positive thứ hai, nên target của SDM gần như luôn là one-hot. Loss đối chứng MPCE (cùng target với SDM, nhưng KL theo chiều ngược lại) cho kết quả gần như trùng InfoNCE (chênh trung bình 0.18 R@1) và kém SDM **3.15 R@1**. Vậy lợi thế của SDM đến từ **chiều của KL**, không đến từ multi-positive.
3. **Cơ chế.** Khi target là one-hot, SDM ≈ λ·(1 − p) − H(p), tức một loss kiểu **MAE** (bị chặn, bền với nhiễu) cộng với **entropy bonus**. SDM giảm trọng số các cặp quá khó hoặc mơ hồ và không để model quá tự tin. Nhờ vậy SDM không overfit, còn InfoNCE và MPCE tụt khoảng 6.6 R@1 sau epoch 3.

---

## 1. Bối cảnh và mục tiêu

- **Bài toán:** Text-Based Person Search (TBPS). Đầu vào là một câu mô tả, ví dụ "a woman in a white coat carrying a black backpack". Hệ thống xếp hạng ảnh người đi bộ trong gallery theo mức độ khớp với câu đó. Đây là bài toán cross-modal retrieval điển hình của multimedia database: gallery được encode một lần thành vector, mỗi truy vấn là một lần nearest-neighbour search trong không gian embedding chung.
- **Động lực:** hướng tới **Federated Learning + PEFT cho TBPS**. Ảnh camera thuộc về nhiều đơn vị vận hành khác nhau và thường không được gom về một chỗ, nên model phải được train ngay tại nơi giữ dữ liệu.
- **Vấn đề của FL:** ở mỗi round, mỗi client phải nhận và gửi lại toàn bộ phần tham số được train, lặp lại hàng chục round. Nếu full fine-tune CLIP, mỗi client phải gửi **571 MiB mỗi round**.
- **Tiền đề cần kiểm chứng trước khi làm FL:** *phần train nhỏ hơn rất nhiều mà độ chính xác giảm không đáng kể.* Báo cáo kiểm chứng tiền đề này ở setting centralized, nơi có thể đo sạch sẽ.
- **Hai câu hỏi nghiên cứu:**
  - **Q1:** LoRA + SDM mất bao nhiêu độ chính xác so với full fine-tune của IRRA, và tiết kiệm được bao nhiêu?
  - **Q2:** Vì sao SDM tốt hơn InfoNCE? Câu hỏi này quan trọng cho FL, vì phải biết SDM tốt *vì sao* thì mới đoán được nó còn tốt hay không trên các client có ít ảnh cho mỗi người.

## 2. Phần có sẵn và phần của em

Khớp với Bảng I của báo cáo (chia 3 nhóm) và nhãn [Existing] / [Ours] trên tiêu đề các section và các khối poster.

| Nhóm | Có sẵn (nguồn) | Của em |
|---|---|---|
| Model | CLIP ViT-B/16 (Radford et al.); ảnh 384×128, τ = 0.02 (IRRA); LoRA (Hu et al.) | Đóng băng backbone, gắn LoRA vào Q/K/V/O của **cả hai** encoder; chọn rank, α, lịch học; toàn bộ code train và eval |
| Lý thuyết | InfoNCE (Oord et al.); SDM và lý do multi-positive (IRRA); MAE bền với nhiễu (Ghosh et al.); confidence penalty (Pereyra et al.) | Tỉ lệ positive trong batch (Eq. 6); khai triển SDM khi target one-hot thành MAE + entropy bonus (Eq. 7); đạo hàm (Eq. 8); MPCE làm loss đối chứng (Eq. 9) |
| Thử nghiệm | RSTPReid và protocol đánh giá; kết quả full fine-tune của IRRA (trích từ paper, không chạy lại) | Toàn bộ run LoRA; ablation InfoNCE / MPCE / SDM; tính chi phí tham số, lưu trữ và truyền thông FL |

## 3. Setup

| Thành phần | Giá trị |
|---|---|
| Backbone | CLIP ViT-B/16 (`openai/clip-vit-base-patch16`), **đóng băng**, 149.6M tham số |
| LoRA | r = 4, α = 8, gắn vào q/k/v/out_proj của 12 layer × 2 encoder → **96 module, 491,520 tham số** |
| Loss | Chỉ SDM, không dùng ID loss và IRR (ablation thay bằng InfoNCE hoặc MPCE) |
| Dữ liệu | RSTPReid: train 3,701 ID × 5 ảnh × 2 caption = 37,010 mẫu; test gồm 1,000 ảnh gallery và 2,000 query |
| Train | AdamW, lr 1e-4, wd 0.02, batch 64, warmup 3 epoch rồi cosine, AMP, seed 42, khoảng 7 phút/epoch trên Colab |
| Đánh giá | R@1/5/10, mAP, mINP sau mỗi epoch. **Peak** là epoch có R@1 cao nhất (cách IRRA báo cáo). **Converged** là trung bình ± độ lệch chuẩn của 6 epoch cuối (con số trung thực hơn) |
| Nhiễu đo | R@1 trên 2,000 query có sai số chuẩn khoảng **1.1 điểm**. Chênh lệch dưới khoảng 2 điểm nên xem là ngang nhau |

Từ ma trận LoRA tới số tham số: mỗi module có r·(d + d) tham số. Image encoder (d = 768) có 48 × 4 × 1536 = 294,912; text encoder (d = 512) có 48 × 4 × 1024 = 196,608. Tổng là 491,520. Sau khi train, BA có thể cộng thẳng vào W, nên chi phí inference bằng đúng CLIP gốc.

---

## 4. Kết quả Q1: LoRA so với full fine-tune

### 4.1 So với IRRA (RSTPReid, text→image, %)

| Method | Tuning | Loss | Trainable | Lưu trữ | R@1 | R@5 | R@10 | mAP | mINP |
|---|---|---|---|---|---|---|---|---|---|
| IRRA: CLIP baseline | full | InfoNCE | 149.6M | 571 MiB | 54.05 | 80.70 | 88.00 | 43.41 | 22.31 |
| IRRA: chỉ SDM | full | SDM | 149.6M | 571 MiB | **57.20** | 79.90 | 88.10 | – | – |
| IRRA: model đầy đủ | full | SDM+ID+IRR | > 165M | > 630 MiB | 60.20 | 81.30 | 88.20 | 47.17 | 25.28 |
| **Ours** (ep. 3) | LoRA r4 | InfoNCE | 0.49M | 1.88 MiB | 55.20 | 76.65 | 85.25 | 42.15 | 20.64 |
| **Ours** (ep. 3) | LoRA r4 | MPCE | 0.49M | 1.88 MiB | 55.70 | 76.40 | 85.50 | 42.35 | 20.78 |
| **Ours** (ep. 9) | LoRA r4 | SDM | 0.49M | 1.88 MiB | **58.85** | 80.30 | **89.15** | 45.46 | 23.29 |

Số của IRRA lấy từ paper (Table 3, 4, 5), em không chạy lại.

**Cách đọc bảng:**
- Phép so sánh công bằng là **LoRA + SDM với IRRA chỉ dùng SDM**, vì cả hai đều chỉ có loss SDM: 58.85 (peak) và 57.18 ± 0.28 (converged), so với 57.20.
  - Peak cao hơn 1.65 điểm, khoảng 1.5 lần sai số chuẩn. Con số converged thì gần như trùng.
  - Vì chỉ có 1 seed, em kết luận là **ngang nhau**, không khẳng định LoRA tốt hơn.
- So với IRRA đầy đủ, LoRA + SDM kém **1.35 R@1** và **1.71 mAP**. Khoảng cách này đến từ ID loss và module IRR. Hai thành phần này mang thêm tham số: ID head 1.90M (gấp khoảng 4 lần ngân sách LoRA), IRR 13.66M.
- **R@10 của LoRA + SDM (89.15) cao nhất bảng**, cao hơn cả IRRA đầy đủ (88.20).

### 4.2 Ý nghĩa chi phí cho FL (tính từ số tham số, fp32, K = 15 client tương ứng 15 camera, R = 30 round)

| | Full FT | LoRA r4 | Tỉ lệ |
|---|---|---|---|
| Tham số train | 149.6M | 0.49M | 304× |
| Upload mỗi client mỗi round | 571 MiB | 1.88 MiB | 304× |
| Upload mỗi round (15 client) | 8.4 GiB | 28.1 MiB | 304× |
| Upload sau 30 round | 251 GiB | 0.82 GiB | 304× |
| Trạng thái AdamW mỗi client | 1.11 GiB | 3.75 MiB | 304× |

**Câu dễ nhớ:** *một round LoRA của cả 15 client vẫn nhỏ hơn 20 lần so với một lần upload full model của một client.* Bảng chỉ tính upload; nếu tính cả download từ server thì lưu lượng gấp đôi.

---

## 5. Kết quả Q2: ablation loss

### 5.1 Bảng tổng hợp (LoRA r4, chỉ khác loss)

| Loss | Target | Divergence | Peak R@1 (epoch) | Peak mAP | Converged R@1 | Tụt từ peak đến cuối |
|---|---|---|---|---|---|---|
| InfoNCE | diagonal (one-hot) | CE | 55.20 (3) | 42.15 | 48.52 ± 0.25 | **−6.60** |
| MPCE | theo identity | KL(q‖p), forward | 55.70 (3) | 42.35 | 48.85 ± 0.15 | **−6.70** |
| SDM | theo identity | KL(p‖q), reverse | **58.85** (9) | **45.46** | **57.18 ± 0.28** | −1.90 |

### 5.2 Diễn biến theo epoch (R@1 %)

| Epoch | 1 | 3 | 4 | 6 | 9 | 12 | 15 | 20 | cuối |
|---|---|---|---|---|---|---|---|---|---|
| SDM | 42.65 | 52.55 | 55.50 | 54.75 | **58.85** | 56.65 | 57.55 | 56.95 | 56.95 (ep 20) |
| MPCE | 41.60 | **55.70** | 53.65 | 52.40 | 51.05 | 51.05 | 50.40 | 49.15 | 49.00 (ep 30) |
| InfoNCE | 42.20 | **55.20** | 53.80 | 53.40 | 51.75 | 51.20 | 49.80 | 49.10 | 48.60 (ep 27) |

### 5.3 Ba cặp so sánh có kiểm soát

Thiết kế ablation gồm hai phép so sánh, mỗi phép chỉ thay đổi đúng một yếu tố:

```
InfoNCE ──(chỉ đổi target: one-hot → theo identity)──► MPCE ──(chỉ đổi chiều KL: forward → reverse)──► SDM
            Δ ≈ 0  (0.18 ± 0.59 R@1)                                Δ = +3.15 R@1, +3.11 mAP
```

1. **Target theo identity không đóng góp gì đo được.** MPCE và InfoNCE dùng cùng lịch học nên so được từng epoch. Trên 27 epoch, R@1 chênh trung bình **0.18 ± 0.59** (lớn nhất 1.45) và mAP chênh 0.17 (lớn nhất 0.64), đều nằm trong mức nhiễu. Tỉ số training loss MPCE/InfoNCE luôn nằm trong khoảng **2.03–2.12**, đúng như lý thuyết dự đoán: bằng đúng 2 với dòng one-hot, cao hơn một chút do 1.52% dòng có positive thứ hai. Đây là xác nhận thực nghiệm rằng target gần như luôn là one-hot.
2. **Chiều KL giải thích toàn bộ phần lợi thế.** SDM hơn MPCE **+3.15 R@1 / +3.11 mAP**, và hơn InfoNCE **+3.65 R@1 / +3.31 mAP**. Mức tăng này tương đương **+3.15** mà IRRA báo cáo khi full fine-tune. Vậy LoRA vẫn giữ được lợi ích của SDM.
3. **Mẫu hình overfitting.** InfoNCE và MPCE đạt peak ở epoch 3 (vừa hết warmup), sau đó tụt khoảng 6.6 điểm, trong khi training loss vẫn giảm đều (InfoNCE từ 2.10 xuống 0.29). Đây là overfitting kinh điển. SDM thì tăng tiếp đến epoch 9 và kết thúc chỉ cách peak 1.90 điểm.

**Phản biện về lịch learning rate.** Run SDM dùng lịch 20 epoch, hai run kia dùng 30 epoch. Tuy vậy, warmup giống hệt nhau, và trong epoch 4–9 LR của hai lịch lệch nhau **tối đa 18%**. Trong cùng đoạn đó, SDM tăng từ 55.50 lên 58.85, còn InfoNCE giảm từ 53.80 xuống 51.75. Hai đường đi ngược chiều nhau, nên chênh lệch LR nhỏ như vậy không giải thích được kết quả.

---

## 6. Key insights

| # | Insight | Bằng chứng |
|---|---|---|
| 1 | LoRA r4 với 0.33% tham số ≈ full fine-tune khi cùng dùng SDM | 58.85 / 57.18 so với 57.20 (Bảng 4.1) |
| 2 | Với random sampling, target của SDM gần như luôn one-hot | 1.52% dòng có positive thứ hai (công thức mục 7.1); tỉ số loss MPCE/InfoNCE ≈ 2.03–2.12 |
| 3 | Khi target one-hot, SDM **không** rút gọn về InfoNCE | Khai triển SDM ≈ λ(1−p) − H(p); có unit test kiểm chứng |
| 4 | Lợi thế của SDM đến từ **chiều KL**, không từ multi-positive | MPCE ≈ InfoNCE (Δ 0.18); SDM − MPCE = +3.15 |
| 5 | InfoNCE overfit nhanh trên dataset nhỏ; SDM thì không | Mức tụt từ peak: −6.60 (InfoNCE) và −6.70 (MPCE) so với −1.90 (SDM) |
| 6 | SDM không có tham số gắn với tập identity toàn cục, nên đưa vào FedAvg không cần sửa gì | Khác ID classifier: 512 × 3701 ≈ 1.90M tham số |

Lưu ý khi trình bày: insight 2–4 **mâu thuẫn với giải thích của IRRA**. IRRA cho rằng SDM tốt vì coi mọi cặp cùng identity trong batch là positive. Đây là điểm mới nhất của báo cáo, nên nhấn mạnh.

---

## 7. Vì sao SDM tốt? (giải thích từng bước)

### 7.1 Bước 1: positive thứ hai hiếm đến mức nào?

Mỗi identity có 10 mẫu trong tổng số N = 37,010. Batch có B = 64 mẫu, lấy ngẫu nhiên. Xác suất một dòng có thêm ít nhất một mẫu cùng identity là:

$$
1-\prod_{k=0}^{B-2}\frac{N-10-k}{N-1-k} = 1.52\%
$$

Nghĩa là **98.48% số dòng** có target q là one-hot e_i, giống hệt target của InfoNCE. Với các dòng này, nếu SDM khác InfoNCE thì sự khác biệt phải đến từ *dạng của loss*, không phải từ target.

### 7.2 Bước 2: SDM khi target one-hot

SDM của dòng i là KL(p_i ‖ q_i + ε), với ε = 1e-8. Thay q_i = e_i và đặt λ = log(1/ε) = **18.42**:

$$
\ell^{sdm}_i = \sum_j p_{ij}\log p_{ij} + \lambda\sum_{j\ne i}p_{ij} - p_{ii}\log(1+\epsilon)
\;\approx\; \underbrace{\lambda(1-p_{ii})}_{\text{MAE có hệ số}} \;-\; \underbrace{H(p_i)}_{\text{entropy bonus}}
$$

So sánh với InfoNCE: ℓ^nce_i = −log p_ii.

- **Thành phần MAE:** 1 − p_ii = ½‖p_i − e_i‖₁ chính là mean absolute error. MAE là loss **bị chặn và đối xứng**, nên đã được chứng minh là bền với label noise (Ghosh et al., 2017). Ngược lại, −log p có thể tăng vô hạn khi p → 0.
- **Thành phần −H(p):** thưởng cho phân phối có entropy cao, chính là **confidence penalty** của Pereyra et al. (2017). Trọng số tương đối của nó so với MAE là 1/λ ≈ 0.05.
- InfoNCE và SDM có **cùng nghiệm tối ưu** p_i = e_i, nhưng trọng số dành cho từng mẫu thì rất khác nhau.

### 7.3 Bước 3: đạo hàm, điểm khác biệt cốt lõi

Lực đẩy lên logit của cặp đúng z_ii:

| Loss | Lực trên cặp đúng | Khi p_ii → 0 (cặp rất khó hoặc mơ hồ) |
|---|---|---|
| InfoNCE | (1 − p_ii) | **lớn nhất**, gần 1 |
| SDM (thành phần MAE) | λ · p_ii · (1 − p_ii) | **gần 0** |

Một vài giá trị cụ thể (λ = 18.42), để thấy hình dạng của hai hàm:

| p_ii | 0.01 | 0.1 | 0.3 | 0.5 | 0.9 |
|---|---|---|---|---|---|
| InfoNCE: 1 − p | 0.99 | 0.90 | 0.70 | 0.50 | 0.10 |
| SDM: λp(1 − p) | 0.18 | 1.66 | 3.87 | **4.61** (max) | 1.66 |
| Tỉ lệ SDM/InfoNCE = λp | 0.18 | 1.84 | 5.53 | 9.21 | 16.6 |

Với Adam, độ lớn tuyệt đối của loss không quan trọng. Điều quan trọng là **cách phân bổ gradient giữa các cặp**:
- **InfoNCE dồn gradient vào các cặp tệ nhất** (p nhỏ).
- **SDM dồn gradient vào các cặp model "đã nhận ra được một nửa"** (p quanh 0.5) và gần như bỏ qua các cặp không thể khớp.

Đạo hàm chính xác (đầy đủ, không xấp xỉ): ∂ℓ^sdm_i/∂z_ij = p_ij · (log p_ij − log q̃_ij − ℓ^sdm_i).

### 7.4 Bước 4: vì sao điều đó giúp trên RSTPReid

- Trong TBPS, các cặp "rất khó" thường là **cặp mơ hồ** hơn là cặp mang nhiều thông tin. Ví dụ: hai người mặc gần giống hệt nhau, hoặc caption bỏ sót đúng chi tiết duy nhất để phân biệt. RSTPReid cũng nhỏ, chỉ khoảng 37k mẫu.
- InfoNCE dùng gradient lớn nhất để ép các cặp này khớp, nên model **học thuộc lòng** chúng. Kết quả là training loss tiếp tục giảm (2.10 → 0.29) nhưng R@1 trên test tụt 6.6 điểm sau epoch 3.
- SDM có thành phần MAE bị chặn, nên giảm trọng số các cặp đó. Entropy bonus thì ngăn phân phối similarity trở nên quá nhọn. Kết quả là model **tiếp tục tổng quát hóa** đến epoch 9 và giữ được mức đó.
- **Vì sao MPCE không giúp được:** MPCE dùng KL(q‖p) = −Σ q log p + const. Khi q là one-hot, MPCE đúng bằng 2 × InfoNCE, mà Adam bất biến khi nhân loss với một hằng số. Vì vậy MPCE có cùng điểm yếu −log p như InfoNCE và tụt y hệt.

**Mức độ chắc chắn:** cơ chế ở 7.4 là **giả thuyết khớp với dữ liệu**, chưa được tách riêng bằng thí nghiệm. Cách kiểm chứng: (a) đổi ε, tức đổi λ, để thay đổi trọng số giữa MAE và entropy; (b) train riêng từng thành phần.

## 8. SDM học được gì?

Nói theo cách trực quan:

1. **SDM học một *phân phối* similarity "đúng chỗ", chứ không cố tạo khoảng cách logit thật lớn.** KL(p‖q) là reverse KL, có tính *mode-seeking*: nó phạt rất nặng (λ = 18.42 cho mỗi đơn vị xác suất) khi đặt xác suất lên các caption không cùng identity. Ngược lại, nó không đòi p_ii phải tiến tới 1 bằng mọi giá, vì thành phần MAE bị chặn và gần như bão hòa khi p_ii đã lớn.
2. **SDM học từ các cặp "học được" thay vì các cặp mơ hồ.** Gradient tập trung ở vùng p ≈ 0.3–0.9, nên embedding được kéo theo các đặc trưng ổn định như màu áo hay đồ mang theo, thay vì bị bóp méo để khớp các caption mơ hồ.
3. **SDM giữ được độ "mềm" (calibration).** Entropy bonus ngăn model quá tự tin, nên phân phối similarity trên tập test không sụp đổ như của InfoNCE.
4. **Với 1.52% dòng có positive thứ hai, SDM vẫn xử lý đúng:** nó không đẩy ảnh cùng người ra xa như negative. Tuy vậy, trên RSTPReid với random sampling, đóng góp này nhỏ đến mức không đo được (đó là kết luận từ MPCE ≈ InfoNCE).

**Câu một dòng cho slide:** *SDM learns where the probability mass should go, not how far apart the logits can be pushed. It ignores pairs it cannot match and stays uncertain where it should.*

---

## 9. SDM trong FedAvg: vì sao có thể tốt?

### 9.1 Lập luận từ báo cáo (đã có trong PDF, Sec. V-D)

1. **Không có tham số gắn với tập identity toàn cục.** ID classifier của IRRA có một hàng cho mỗi trong 3,701 identity. Trong FL, mỗi client chỉ thấy một phần nhỏ các identity, nên rất nhiều hàng không được client nào cập nhật đúng, và việc lấy trung bình chúng là vô nghĩa. Classifier này còn làm upload tăng khoảng 4 lần (1.90M so với 0.49M). SDM không có tham số, chỉ cần quan hệ y_i = y_j trong batch cục bộ, nên **train cục bộ và FedAvg mà không phải sửa gì**.
2. **Lợi thế của SDM không phụ thuộc multi-positive.** Mục 5 cho thấy lợi thế đến từ chiều KL. Vì vậy, khi mỗi client chỉ có ít ảnh cho mỗi người, không có lý do gì để lợi thế đó biến mất.
3. **Tiết kiệm 304 lần lưu lượng** (Bảng 4.2), cộng với 3.75 MiB trạng thái optimizer, phù hợp với thiết bị ở phía camera.

### 9.2 Bằng chứng sơ bộ từ các run FedAvg (KHÔNG có trong báo cáo PDF)

Các run FedAvg sơ bộ đều dùng **SDM**. Các run này được chạy trước khi thêm tuỳ chọn `--loss`, và khi đó SDM là loss duy nhất. Thang loss khoảng 15–25 cũng khớp với thang của SDM. Setup: chia theo camera thành 15 client, 1 local epoch mỗi round, lr 1e-4, batch 64.

| Run | Rank | Round | R@1 | mAP | Upload tích lũy |
|---|---|---|---|---|---|
| FedAvg (`B5_camera_lora4_v1`) | 4 | 5 / 10 / 15 / 20 | 46.95 / 52.55 / 54.15 / 56.00 | 36.60 / 40.26 / 42.05 / 43.34 | 141 / 281 / 422 / 563 MiB |
| | 4 | 25 | 57.05 | 44.23 | 703 MiB |
| | 4 | 30 | **57.05** | **44.63** | **844 MiB** |
| FedAvg (`r8`, cosine) | 8 | 35 | 57.40 | 44.91 | 1,969 MiB |
| *Centralized (báo cáo)* | 4 | conv. | *57.18 ± 0.28* | *45.42* | – |
| *Full FT FedAvg (ước tính)* | – | 30 | – | – | *251 GiB* |

**Nhận xét:**
- **FedAvg LoRA + SDM r4 đạt 57.05 R@1 sau 30 round, gần như bằng centralized converged (57.18)**, với tổng upload chỉ 844 MiB. Con số này nhỏ hơn một lần upload full model của 2 client.
- Đường R@1 của FedAvg **tăng đều, không tụt**: r8 đi từ 27.00 ở round 1 lên 57.40 ở round 35. Đây là cùng mẫu hình "không overfit" như SDM ở chế độ centralized.
- r8 hơn r4 chỉ 0.35 điểm, trong mức nhiễu, nhưng tốn gấp đôi lưu lượng. **r = 4 là đủ.**
- Phân hoạch dữ liệu non-IID khá mạnh:
  - Số ảnh mỗi client dao động từ 56 đến 3,265 (hệ số biến thiên 0.85).
  - Độ trùng identity giữa các client thấp: Jaccard trung bình theo cặp là 0.12.
  - Trung bình chỉ có 2–3.6 caption cho mỗi identity trên mỗi client.

### 9.3 Một điểm tinh tế: multi-positive trên client nhỏ

Ước lượng tỉ lệ dòng có positive thứ hai trong batch 64 trên từng client. Đây là xấp xỉ, giả định số mẫu mỗi identity đều nhau trong client:

| Client | Số ảnh | Số ID | Ước lượng % dòng có positive thứ hai |
|---|---|---|---|
| 1 (lớn) | 3,071 | 2,421 | khoảng 1.6% |
| 9 | 115 | 114 | khoảng 28% |
| 2 (nhỏ nhất) | 56 | 53 | khoảng 61% |
| Trung bình có trọng số (15 client) | | | khoảng 3.3% |

Trên client nhỏ, một batch phủ gần hết dữ liệu của client, nên **caption thứ hai của cùng ảnh thường nằm chung batch**. Khi đó InfoNCE sẽ đẩy chính caption đúng ra xa như một negative, còn SDM coi nó là positive. Vì vậy, trong FL, target theo identity của SDM có thể có ích hơn so với setting centralized. Đây là **giả thuyết** cần kiểm chứng.

### 9.4 Giới hạn và thí nghiệm nên làm tiếp

- **Chưa có run FedAvg với InfoNCE.** Do đó chưa thể khẳng định FedAvg tốt *nhờ* SDM; hiện chỉ biết FedAvg + SDM ≈ centralized + SDM.
- Mỗi cấu hình chỉ có 1 seed. Run r4 đánh giá 5 round một lần, và r4/r8 dùng lịch LR khác nhau.
- **Thí nghiệm đề xuất:** chạy lại FedAvg r4 với `--loss infonce` và `--loss mpce`, giữ nguyên partition camera (code đã có sẵn tuỳ chọn này):
  ```bash
  python -m experiments.clip_lora_fedavg.main --root /content/RSTPReid \
    --partition camera --num_clients 15 --rounds 30 --lora_rank 4 \
    --loss infonce --out_dir /content/drive/MyDrive/runs/fl_r4_infonce
  ```
  Nếu InfoNCE trong FL tụt sớm như ở centralized, còn SDM thì không, thì kết luận "SDM chống overfit và chống client drift" sẽ có bằng chứng trực tiếp.

---

## 10. Hạn chế (nên nói chủ động khi trình bày)

- Mỗi run chỉ có 1 seed; sai số chuẩn của R@1 khoảng 1.1. Các khoảng cách SDM–InfoNCE và SDM–MPCE (khoảng 3 lần sai số chuẩn) đáng tin hơn, và mAP (ít nhiễu hơn) cũng cho cùng kết quả.
- Run SDM dùng lịch 20 epoch, hai run còn lại dùng 30 epoch (đã phản biện ở mục 5.3).
- Peak được chọn trên tập test, giống cách IRRA làm, nên hơi lạc quan. Vì vậy báo cáo luôn kèm con số converged.
- Số của IRRA lấy từ paper, em không chạy lại.
- Cơ chế MAE + entropy chưa được tách riêng bằng thí nghiệm.
- Kết luận chỉ đúng cho RSTPReid với random sampling. Với identity sampler (P×K), target multi-positive sẽ xuất hiện thường xuyên và có thể có tác dụng.

---

## 11. Gợi ý kịch bản thuyết trình (khoảng 12–15 phút, 11 slide)

| # | Slide | Nội dung chính | Thời gian |
|---|---|---|---|
| 1 | Title | Tên đề tài, tác giả, mã học viên | 0:20 |
| 2 | Bài toán TBPS | Ví dụ query → gallery; cross-modal retrieval trong multimedia DB | 1:00 |
| 3 | Động lực FL | Vì sao cần FL + PEFT cho TBPS; 571 MiB mỗi client mỗi round; tiền đề cần chứng minh; Q1 và Q2 | 1:30 |
| 4 | Có sẵn và của em | Bảng mục 2 | 1:00 |
| 5 | Method | Hình pipeline (Fig. 1); LoRA với 96 module và 0.49M tham số; chỉ dùng SDM | 1:30 |
| 6 | Kết quả Q1 | Bảng 4.1, nhấn mạnh 58.85 / 57.18 so với 57.20; 304× | 1:30 |
| 7 | Chi phí FL | Bảng 4.2; "một round LoRA < 1/20 lần upload full của một client" | 1:00 |
| 8 | Câu hỏi Q2 + insight 1.52% | IRRA nói gì; công thức xác suất; 98.48% dòng one-hot | 1:30 |
| 9 | SDM ≠ InfoNCE | Khai triển λ(1−p) − H(p); bảng trọng số gradient (mục 7.3) | 2:00 |
| 10 | Ablation | Sơ đồ InfoNCE → MPCE → SDM; Fig. 2 (các đường cong); tụt −6.6 so với −1.9 | 2:00 |
| 11 | FedAvg + kết luận | Mục 9.1 và 9.2: 57.05 sau 30 round với 844 MiB; 3 thông điệp; hướng tiếp theo | 1:30 |

## 12. Câu hỏi có thể gặp và gợi ý trả lời

| Câu hỏi | Gợi ý trả lời |
|---|---|
| Sao không chạy lại IRRA? | Giới hạn GPU (Colab). So sánh với dòng "chỉ SDM" trong ablation của chính IRRA là phép so sánh công bằng nhất có thể. Em nói rõ là số trích từ paper. |
| Peak chọn trên test có gian lận không? | Đó là cách IRRA báo cáo. Em kèm thêm con số converged (trung bình 6 epoch cuối, không chọn epoch): 57.18, vẫn ngang 57.20. |
| 1 seed thì sao tin được? | Chênh LoRA so với full FT nhỏ hơn 2 lần sai số chuẩn nên em chỉ kết luận ngang nhau. Chênh SDM so với InfoNCE và MPCE khoảng 3 lần sai số chuẩn, mAP cũng cho cùng chiều, và cả đường cong (không chỉ một điểm) đều khác biệt rõ. |
| Lịch LR khác nhau có phải nguyên nhân? | Trong epoch 4–9, LR lệch tối đa 18% nhưng hai đường đi ngược chiều nhau. Warmup giống hệt nhau. |
| MAE nổi tiếng là underfit, sao ở đây lại tốt? | Ở đây MAE được áp lên một backbone CLIP đã pre-train mạnh, nên phần lớn cặp đã có p không quá nhỏ ngay từ đầu. Entropy bonus thì giữ gradient không chết. Trên dataset nhỏ và nhiễu, tính bền quan trọng hơn tốc độ khớp. |
| ε = 1e-8 có ý nghĩa gì? | Nó quyết định λ = log(1/ε) = 18.42, tức trọng số giữa MAE và entropy. Đổi ε là một thí nghiệm kiểm chứng tự nhiên cho cơ chế. |
| Tại sao không dùng ID loss để bù 1.35 điểm? | ID head có 1.90M tham số (gấp 4 lần LoRA) và gắn với tập identity toàn cục, nên không phù hợp với FL. |
| FL có non-IID không? | Có, chia theo camera: số ảnh mỗi client từ 56 đến 3,265, Jaccard identity 0.12. Dù vậy FedAvg r4 vẫn đạt 57.05, gần bằng centralized. Đây là kết quả sơ bộ, nằm ngoài báo cáo. |

---

## 13. Nguồn số liệu

| Số liệu | Nguồn |
|---|---|
| 3 run loss | `final-report/results/{sdm,infonce,mpce}_log.csv` → `generated/numbers.tex`, `generated/curve_*.csv` |
| IRRA | arXiv 2303.12501, Table 3, 4, 5 |
| Chi phí FL | `scripts/gen_results.py` (tính từ số tham số) |
| FedAvg r4 / r8 | Log của run `B5_camera_lora4_v1_20262308` và `r8` (`log.csv`, `partition_stats.json`) |
| % positive thứ hai theo từng client (mục 9.3) | Ước lượng xấp xỉ từ `partition_stats.json`; không phải số đo thực nghiệm |
