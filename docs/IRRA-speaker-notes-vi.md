- **Slide 1 — Title**
  - Dẫn: không cần dẫn — đây là câu mở đầu buổi nói.
  - **Text-to-Image Person Retrieval** — truy hồi ảnh người từ mô tả văn bản: đầu vào một câu, đầu ra là ảnh.
  - **Implicit Relation Reasoning** — suy luận quan hệ ẩn; chữ "ẩn" là điểm mấu chốt của cả bài báo, giải thích kỹ ở slide 7.
  - **IRRA** — viết tắt của **I**mplicit **R**elation **R**easoning and **A**ligning (Ding Jiang, Mang Ye, CVPR 2023).
  - Thông điệp cần gieo: mô hình học tương tác chi tiết **trong lúc train**, nhưng khi triển khai vẫn chỉ so một vector ảnh với một vector text — cân bằng giữa độ chính xác và chi phí truy hồi.

- **Slide 2 — I. Introduction — From Description to Top-k**
  - Dẫn: "Hãy tưởng tượng một nhân viên an ninh cần tìm một người trong kho camera, nhưng trong tay không hề có ảnh của người đó — chỉ có lời kể của nhân chứng."
  - **Query (truy vấn)** — thứ người dùng đưa vào; ở đây **không phải ảnh** mà là một câu tiếng Anh tự do. Đây là điểm khác biệt so với Re-ID truyền thống.
  - **Gallery** — kho ảnh cần tìm kiếm trong đó; trong các benchmark của bài báo có từ vài nghìn đến gần hai mươi nghìn ảnh.
  - **Ranked image list (Top-k)** — đầu ra **không phải một đáp án duy nhất** mà là danh sách ảnh xếp theo độ phù hợp giảm dần; người dùng nhìn 10 ảnh đầu và tự chọn.
  - **Cross-modal retrieval** — truy vấn thuộc một modality (văn bản), kết quả thuộc modality khác (ảnh); chính điều này khiến bài toán khó hơn tìm ảnh-bằng-ảnh.
  - **Person Re-ID** (nhắc để đối chiếu, không có trên slide) — đưa vào một **ảnh** người, tìm ảnh cùng người ở camera khác. Có ảnh truy vấn thì dùng Re-ID; bài toán hôm nay là khi **không có** ảnh đó.
  - **Hai dải Baseline / IRRA** — cùng một truy vấn, hàng dưới đẩy được nhiều ảnh đúng lên cao hơn. Chưa giải thích vì sao — để dành cho phần sau.

- **Slide 3 — I. Introduction — Multimedia Database Perspective**
  - Dẫn: "Đây là slide gắn bài báo với học phần của chúng ta. Một hệ thống truy hồi đa phương tiện luôn có hai pha, và bài báo chỉ can thiệp vào đúng một trong hai."
  - **Pha offline — lập chỉ mục gallery** — toàn bộ ảnh đi qua image encoder **một lần duy nhất**, mỗi ảnh thành một vector 512 chiều được lưu lại và có thể xây chỉ mục lên trên; chạy trước, không liên quan người dùng.
  - **Embedding / feature vector** — biểu diễn số của một đối tượng đa phương tiện; toàn bộ ý nghĩa tấm ảnh bị nén vào một dãy số, chất lượng hệ thống phụ thuộc hoàn toàn vào việc dãy số này có "đúng" hay không.
  - **Pha online — xử lý truy vấn** — câu mô tả được mã hóa **một lần** thành vector cùng chiều, cùng không gian; tính tương đồng với toàn bộ vector ảnh đã lưu rồi trả Top-k.
  - **Cosine similarity** — $\operatorname{sim}(f^v,f^t)=\frac{(f^v)^\top f^t}{\lVert f^v\rVert\,\lVert f^t\rVert}$; đo **góc** chứ không đo độ dài, giá trị −1…1, càng gần 1 càng giống. Vì đã chuẩn hóa nên bền với việc encoder xuất vector có norm khác nhau.
  - **Joint embedding space (không gian nhúng chung)** — điều kiện tiên quyết để cosine có nghĩa: vector ảnh và vector chữ phải nằm cùng một không gian. Toàn bộ việc huấn luyện là để tạo ra không gian này.
  - **Chỉ mục vector / ANN** — HNSW, IVF, FAISS… giúp không phải quét tuyến tính toàn bộ gallery. **Bài báo không nghiên cứu phần này** — IRRA chỉ cải tiến hai khối encoder.
  - Nếu bị hỏi "bài báo có làm hệ thống nhanh hơn không": **bằng** CLIP dual encoder về chi phí inference nhưng chính xác hơn; chỉ nhanh hơn so với nhóm explicit local matching vốn phải lưu và so nhiều vector cục bộ.

- **Slide 4 — I. Introduction — Why Is the Task Difficult?**
  - Dẫn: "Có bốn khó khăn, hai khó khăn đầu đến từ **dữ liệu**, hai khó khăn sau đến từ **ngữ nghĩa**."
  - **Intra-identity variation** — cùng một người nhưng hai ảnh rất khác nhau do *viewpoint*, *pose*, *lighting*, *occlusion*. Hệ quả: không thể chỉ học "trông giống nhau thì là một người".
  - **Modality heterogeneity** — ảnh là tín hiệu **liên tục, hai chiều, không thứ tự tự nhiên**; câu là chuỗi **ký hiệu rời rạc, một chiều, thứ tự mang nghĩa**. Không ghép trực tiếp được, buộc phải học ánh xạ về không gian chung.
  - **Subtle discriminative details** — điểm quan trọng nhất: rất nhiều người có mô tả toàn cục gần như giống hệt nhau ("phụ nữ mặc áo sáng màu, quần tối màu"); chỉ phân biệt được bằng chi tiết — túi **trắng** hay **đen**, áo **sọc** hay **trơn**. Biểu diễn toàn cục thô làm nhòe đúng những chi tiết này.
  - **Language ambiguity** — thứ tự thuộc tính tùy ý, có thể bỏ sót thuộc tính, dùng từ đồng nghĩa ("purse" / "handbag" / "bag").
  - **Dòng chốt — mâu thuẫn trung tâm:** muốn phân biệt đúng người → cần **chi tiết cục bộ**; muốn truy hồi nhanh trên gallery lớn → cần **một vector toàn cục duy nhất**. Hai yêu cầu kéo về hai hướng ngược nhau, và cả phần còn lại của bài là câu trả lời cho việc dung hòa chúng.

- **Slide 5 — I. Background — Three Matching Paradigms**
  - Dẫn: "Slide trước kết thúc bằng một mâu thuẫn. Slide này cho thấy hai cách giải quyết đã có, và vì sao cả hai đều chưa đủ."
  - **Global matching** — nén cả ảnh thành một vector, cả câu thành một vector, đặt loss ở cuối mạng. Ưu: cực nhanh khi truy hồi, đúng mô hình CSDL ở slide 3. Nhược: loss chỉ ở **đầu ra cuối cùng**, hai luồng không trao đổi thông tin ở tầng giữa nên chi tiết cục bộ bị "trung bình hóa".
  - **Explicit local matching** — tách ảnh thành vùng (đầu/thân/chân), tách câu thành cụm từ, rồi ghép từng vùng với từng cụm.
    - **Prior (tri thức tiên nghiệm)** — thường là mô hình phụ như *human parsing* hoặc chia ảnh thành dải ngang cố định.
    - **Ba nhược điểm riêng biệt:** (1) **nhiễu từ prior** — phân đoạn sai thì alignment sai theo, lỗi lan truyền; (2) **chi phí lưu trữ** — mỗi ảnh thành *nhiều* vector cục bộ, gallery phình lên; (3) **chi phí so sánh** — ghép cặp nhiều-nhiều rồi tổng hợp, phá vỡ giả định của CSDL vector ở slide 3.
  - **IRRA — hướng thứ ba** — `Implicit local learning during training`: local token **vẫn tương tác rất mạnh** khi train; `Global embeddings at inference`: đầu ra **không có** nhánh local matching nào. Chi tiết được **hấp thụ vào** global embedding qua gradient, thay vì được **giữ lại** thành vector cục bộ riêng.

- **Slide 6 — I. Background — Dual-Stream Models and CLIP**
  - Dẫn: "Trước khi vào phương pháp, cần một khái niệm nền: mô hình thị giác–ngôn ngữ chia làm hai họ, và lựa chọn họ nào quyết định toàn bộ chi phí hệ thống."
  - **Single-stream** — token ảnh và token chữ vào **chung một Transformer** ngay từ đầu; self-attention chạy trên chuỗi hợp nhất nên mọi token ảnh thấy mọi token chữ → tương tác rất mạnh.
  - **Nhược điểm chí mạng của single-stream** — kết quả phụ thuộc vào **cặp**: muốn chấm điểm ảnh A với câu Q phải chạy cả mô hình cho cặp (A, Q). Gallery 20.000 ảnh → một truy vấn cần 20.000 lần chạy Transformer, không tiền tính toán được → không dùng được cho CSDL.
  - **Dual-stream** — hai encoder **độc lập**, mỗi bên tự cho ra một vector, chỉ gặp nhau ở phép cosine cuối cùng. Vì độc lập nên **mã hóa gallery trước** được (đúng pha offline ở slide 3).
  - **CLIP** — *Contrastive Language–Image Pre-training*, mô hình dual-stream train trên lượng rất lớn cặp ảnh–chú thích Internet. Ý nghĩa: **CLIP đã có sẵn một không gian nhúng chung tốt**, không phải học từ đầu.
  - **Nhược điểm của dual-stream** — hai luồng không "nói chuyện" cho tới tận cuối nên tương tác chi tiết bị hạn chế; đúng là nhược điểm của global matching ở slide 5.
  - **Thanh đỏ — luận điểm cả slide:** IRRA lấy toàn bộ CLIP và bổ sung tương tác **chỉ trong lúc huấn luyện** — mượn ưu điểm single-stream mà không trả giá khi triển khai.
  - **"Full CLIP"** — một số công trình trước chỉ mượn image encoder hoặc đóng băng một phần; IRRA fine-tune **cả hai** encoder.
  - Nếu bị hỏi "CLIP train trên ảnh Internet, người trong camera giám sát rất khác — có hợp không": đó là lý do fine-tune toàn bộ chứ không đóng băng; slide 19 cho thấy CLIP fine-tune trực tiếp đã là baseline rất mạnh, trên RSTPReid còn vượt CFine.

- **Slide 7 — II. Proposed Method — Research Question**
  - Dẫn: "Ba slide vừa rồi đã dựng đủ bối cảnh. Giờ ta có thể phát biểu chính xác câu hỏi mà bài báo đặt ra."
  - **Câu hỏi nghiên cứu — ba mệnh đề, đọc chậm từng mệnh đề:**
    - *fine-grained image–word relations* — quan hệ giữa **một từ** và **một vùng ảnh**, ví dụ "white" ↔ vùng chiếc túi → ứng với khó khăn số 3 ở slide 4.
    - *without part-level supervision* — không cần nhãn thủ công kiểu "vùng này là túi", không cần human parsing → ứng với nhược điểm explicit local ở slide 5.
    - *without additional retrieval cost* — khi truy hồi vẫn chỉ một vector ↔ một vector → ràng buộc từ pha online ở slide 3.
  - **Chốt định nghĩa "implicit" — chỗ quan trọng nhất của slide:** *implicit* **không** có nghĩa là "không dùng local token"; ngược lại local token tương tác rất mạnh khi train. Nó có đúng hai nghĩa: (1) **không cần nhãn tường minh** về bộ phận cơ thể hay correspondence từ–vùng, mô hình tự tìm ra; (2) **không có nhánh local matching ở đầu ra** — quan hệ cục bộ chỉ là *tín hiệu huấn luyện*, không phải *thành phần của điểm số truy hồi*.
  - **Ba đóng góp:** **IRR** (Implicit Relation Reasoning, thực hiện bằng MLM — slide 12–13); **SDM** (Similarity Distribution Matching, loss mới — slide 14); **Full CLIP transfer** (fine-tune cả hai encoder).

- **Slide 8 — II. Proposed Method — IRRA Overview**
  - Dẫn: "Đây là sơ đồ tổng thể. Em sẽ đi theo đúng ba số ở dưới slide, và xin khán giả để ý: những khối vẽ bằng **nét đứt** sẽ bị bỏ khi triển khai."
  - **Khối 1 — CLIP dual encoder (xương sống)** — ảnh → ViT → chuỗi visual token, token `[CLS]` là global image embedding $f^v$; câu → Text Encoder → chuỗi text token, token `[EOS]` là global text embedding $f^t$. Đây là phần **duy nhất** còn sống sót khi inference.
  - **Khối 2 — SDM + ID (giám sát cấp toàn cục)** — $f^v, f^t$ vào **SDM loss** (căn chỉnh cross-modal) và vào **ID classifier** (phân loại danh tính); hai loss này tác động **trực tiếp** lên global embedding.
  - **Khối 3 — IRR / MLM (giám sát cấp token)** — có **một bản sao thứ hai của câu** bị che ngẫu nhiên, đi qua **cùng** text encoder (dùng chung tham số); masked text token làm **Query**, visual token làm **Key/Value** → **Multimodal Interaction Encoder** → **MLM head** → dự đoán lại từ bị che. Loss này tác động **gián tiếp** lên global embedding qua đường token.
  - **Ba điểm phải nhấn:** (1) **text encoder chạy hai lần trong một bước huấn luyện** với **cùng bộ tham số** — chi tiết dễ bỏ sót nhất; (2) toàn bộ hệ thống train **end-to-end**, một lần backward duy nhất; (3) **các khối nét đứt — interaction encoder, MLM head, ID classifier — đều bị bỏ khi test**, chỉ còn hai encoder và một phép cosine.

- **Slide 9 — II. Proposed Method — CLIP Dual Encoder**
  - Dẫn: "Ta phóng to khối số một. Câu hỏi rất cụ thể: một tấm ảnh và một câu chữ biến thành vector bằng cách nào?"
  - **ViT-B/16** — Vision Transformer bản Base, patch 16: 12 block, chiều ẩn 768, 12 head.
  - **`384 × 128`** — kích thước ảnh vào, tỷ lệ **3:1 theo chiều dọc** chứ không vuông, vì ảnh người đứng cao hơn rộng — lựa chọn riêng cho person retrieval.
  - **Patch `16 × 16`** — ảnh cắt thành lưới ô 16×16 pixel, mỗi ô làm phẳng và chiếu tuyến tính thành vector 768 chiều; từ đây Transformer không còn "thấy" pixel, chỉ thấy một chuỗi token.
  - **`24 × 8 = 192 visual tokens`** — $384/16=24$ hàng, $128/16=8$ cột; cộng token `[CLS]` là **193 token**.
  - **`[CLS]`** — token đặc biệt **thêm vào** đầu chuỗi, không ứng với vùng ảnh nào; vì self-attention cho nó nhìn mọi patch nên nó dần thành nơi **tổng hợp thông tin toàn ảnh**. Sau khi chiếu, chính là $f^v$.
  - **BPE (Byte Pair Encoding)** — tách văn bản theo mảnh từ xuất hiện nhiều chứ không theo từ; ưu điểm: không bao giờ gặp từ lạ hoàn toàn vì từ hiếm bị tách thành nhiều mảnh.
  - **Vocabulary `49,152`** — ⚠️ con số trong code thực tế là **49,408**.
  - **`[SOS]` / `[EOS]`** — token đánh dấu đầu/cuối câu; câu thật nằm giữa, tối đa **77 token** kể cả hai token đặc biệt.
  - **`[EOS] → f^t`** — hidden state tại `[EOS]` làm vector câu; vì `[EOS]` đứng cuối nên đã "nhìn" qua toàn bộ câu (lý do đầy đủ ở slide 11, liên quan causal mask).
  - **Cùng không gian** — cả hai vector đều chiếu về **512 chiều**, đúng không gian nhúng chung của CLIP.
  - Câu rất dễ quên: các local token (192 visual token và các text token) **không** tham gia tính điểm khi test, nhưng **được giữ lại** để huấn luyện IRR — đây là cầu nối sang slide 12.

- **Slide 10 — II. Proposed Method — Inside the ViT Image Encoder**
  - Dẫn: "Slide trước nói ảnh biến thành 192 token. Slide này nói 192 token đó được xử lý thế nào — và quan trọng hơn, vì sao chúng giữ được thông tin cục bộ."
  - **Positional embedding** — self-attention không biết thứ tự/vị trí; không cộng thông tin vị trí thì mô hình không phân biệt patch vùng đầu với patch vùng chân. Là vector học được, cộng vào từng token.
  - **Pre-LayerNorm (Pre-LN)** — LayerNorm đặt **trước** khối attention/MLP; biến thể chuẩn của CLIP, giúp train mạng sâu ổn định hơn.
  - **MSA — Multi-head Self-Attention** — nói bằng lời, không bằng công thức: mỗi token nhìn vào **tất cả** token khác, tự quyết định token nào đáng chú ý, rồi tổng hợp có trọng số. Cụ thể: patch vùng áo có thể nhìn sang patch vùng túi/quần/giày, `[CLS]` nhìn tất cả. **"Multi-head"** = làm song song 12 lần với 12 phép chiếu khác nhau để mỗi đầu chú ý một loại quan hệ.
  - **Residual connection** — `x + f(x)` thay vì `f(x)`: giữ thông tin gốc không mất qua từng lớp, và tạo "đường cao tốc" cho gradient chảy ngược về lớp đầu. **Đây là lý do kỹ thuật khiến gradient của MLM ở slide 12 đi ngược được tận vào patch embedding.**
  - **MLP `768 → 3072 → 768`** — hai lớp tuyến tính, mở rộng gấp bốn rồi nén lại, activation **QuickGELU** ở giữa. Attention là nơi các token *trao đổi* thông tin, MLP là nơi mỗi token *xử lý riêng* thông tin của mình.
  - **`[CLS]` collects global visual context** — sau 12 vòng lặp, CLS đã tích lũy thông tin từ mọi vùng ảnh.
  - **Đầu ra cuối** — LayerNorm → chiếu 768 → 512; token đầu thành $f^v$, **192 token còn lại giữ nguyên** làm Key/Value cho IRR.

- **Slide 11 — II. Proposed Method — Inside the CLIP Text Encoder**
  - Dẫn: "Cấu trúc block gần như y hệt slide trước, nên em chỉ nói vào đúng một điểm khác biệt — nhưng điểm khác biệt đó lại giải thích một câu hỏi từ slide 9."
  - **Causal self-attention (attention nhân quả)** — token ở vị trí $i$ **chỉ nhìn** được vị trí $1..i$, không nhìn về phía sau; cơ chế là một mặt nạ tam giác che toàn bộ phần tương lai.
  - **Vì sao CLIP làm vậy** — text encoder của CLIP kế thừa thiết kế mô hình ngôn ngữ tự hồi quy (kiểu GPT); IRRA giữ nguyên để tận dụng trọng số pre-train.
  - **Hệ quả — câu trả lời cho slide 9:** vì mỗi token chỉ thấy phần đứng trước, và `[EOS]` là token **cuối cùng**, nên `[EOS]` là token **duy nhất đã nhìn thấy toàn bộ câu**. Đó là lý do lấy hidden state tại `[EOS]` làm vector câu, chứ không lấy trung bình các token hay lấy token đầu.
  - **Phần còn lại của block** — giống hệt ViT: `LN → attention → residual → LN → MLP → residual`; linear projection → $f^t$ 512 chiều, cùng không gian với $f^v$.
  - **Mắt xích logic của cả phần phương pháp** — trong **một** bước huấn luyện, text encoder chạy **hai lượt** với **cùng bộ tham số**: lượt 1 (câu **gốc**) lấy `[EOS]` → $f^t$ cho SDM và ID loss; lượt 2 (câu **bị che**) lấy toàn bộ token làm Query cho interaction encoder → MLM. Khi backward, gradient của **cả hai lượt cộng vào cùng một bộ tham số** — đây chính là cơ chế khiến học MLM cải thiện được $f^t$ dùng khi truy hồi.

- **Slide 12 — II. Proposed Method — IRR through MLM**
  - Dẫn: "Đây là ý tưởng trung tâm của bài báo, và em nghĩ nó rất đẹp: tác giả không phát minh ra một cơ chế alignment mới, mà mượn một bài toán quen thuộc từ NLP rồi đặt nó vào bối cảnh đa phương thức."
  - **MLM — Masked Language Modeling** — bài toán vốn dùng pre-train BERT: che ngẫu nhiên một số từ, bắt mô hình đoán lại.
  - **Khác biệt mấu chốt so với BERT** — BERT chỉ có **ngữ cảnh chữ** để đoán; IRRA có **ngữ cảnh chữ cộng thêm tấm ảnh**. Ví dụ: che `white` trong `a [MASK] purse` — chỉ nhìn chữ thì hàng chục màu đều hợp ngữ pháp, để đoán đúng `white` mô hình **buộc phải** tìm ra vùng ảnh chứa chiếc túi và đọc màu của nó. → **MLM ép mô hình học quan hệ từ ↔ vùng ảnh mà không cần ai gán nhãn vùng nào là cái túi** — đó chính xác là nghĩa của chữ *implicit*.
  - **Ba từ bị che trong ví dụ = ba loại quan hệ khác nhau:** `shoes` — danh từ, tên vật thể → cần nhận diện đối tượng; `white` — tính từ, thuộc tính → cần đọc màu ở đúng vùng; `around` — giới từ, quan hệ không gian → cần hiểu bố cục ("quanh eo").
  - **Quy tắc 15% và 80/10/10** — kế thừa từ BERT: chọn ngẫu nhiên 15% token để dự đoán; trong đó 80% thay bằng `[MASK]`, 10% thay bằng token ngẫu nhiên, 10% giữ nguyên. **Vì sao phức tạp vậy:** nếu luôn thay `[MASK]`, mô hình chỉ học cách xử lý `[MASK]` — mà khi test không có `[MASK]` nào, gây lệch train/test. Trộn thêm token ngẫu nhiên và giữ nguyên buộc mô hình "đề phòng" ở **mọi** vị trí. *(Code: nếu không token nào được chọn thì ép mask ít nhất một token.)*
  - **Hàm loss** — cross-entropy chỉ tính trên vị trí bị chọn: $\mathcal L_{\mathrm{IRR}} = -\frac{1}{|\mathcal M|}\sum_{i\in\mathcal M}\log p_\theta(w_i \mid \hat T, I)$, với $\mathcal M$ là tập vị trí bị che. Code dùng `CrossEntropyLoss(ignore_index=0)` — vị trí không chọn có nhãn 0 và bị bỏ qua.
  - **Figure 3 — cơ chế alignment:** từ thật (`bag`) có embedding **tĩnh**, cố định trong từ điển, đóng vai trò **mỏ neo**. Mô hình phải kéo cả biểu diễn vùng ảnh lẫn biểu diễn ngữ cảnh câu về phía mỏ neo đó; vì cùng bị kéo về một điểm nên chúng **gián tiếp** được kéo lại gần nhau.

- **Slide 13 — II. Proposed Method — Multimodal Interaction**
  - Dẫn: "Slide trước đặt ra yêu cầu: token chữ phải lấy được thông tin từ ảnh. Slide này là cơ chế thực hiện yêu cầu đó."
  - **Q, K, V — giải thích bằng ẩn dụ tra cứu, đừng bằng công thức:** **Q** (Query, "tôi đang cần tìm gì") = hidden state của token trong **câu bị che**; **K** (Key, "tôi chứa nội dung gì") = **visual token** (192 vùng ảnh); **V** (Value, "nội dung thực sự lấy về") = **visual token**. Cơ chế: mỗi Query so khớp toàn bộ Key để tính trọng số chú ý, rồi lấy tổng có trọng số của các Value — $\operatorname{MCA}(Q,K,V)=\operatorname{softmax}\!\big(\tfrac{QK^\top}{\sqrt d}\big)V$.
  - **Diễn giải một câu:** token chữ chủ động **hỏi** ảnh *"vùng nào của bức ảnh liên quan đến tôi?"*, rồi mang thông tin từ vùng đó về.
  - **Cross-attention vs self-attention** — self-attention: Q, K, V cùng một nguồn; cross-attention: Q từ nguồn này, K/V từ nguồn khác. Đây là cách chuẩn để một modality lấy thông tin từ modality khác.
  - **One-way (một chiều)** — chỉ chữ hỏi ảnh, **không** có chiều ngược lại. Lý do thực dụng: nhiệm vụ cuối là **dự đoán token văn bản**, nên chỉ cần làm giàu phía văn bản; chiều ngược lại là dư thừa.
  - **`4 Transformer blocks`** — sau cross-attention, kết quả đi tiếp qua 4 block self-attention + feed-forward để các token văn bản (đã có thông tin ảnh) tiếp tục trao đổi với nhau.
  - **`hidden size = 512`, `8 heads`** — khớp chiều không gian nhúng CLIP, 512 ÷ 64 = 8. *(Code: `nn.MultiheadAttention(512, 512//64)`, `Transformer(width=512, layers=4, heads=8)`, `cmt_depth` mặc định 4.)*
  - **MLM head** — `Linear → QuickGELU → LayerNorm → Linear(vocab_size)`, cho phân phối trên toàn từ điển tại mỗi vị trí bị che.
  - **Ba kiểu module trong Figure 4:** (a) **Co-attention** — hai nhánh Transformer song song hỏi nhau qua lại, nhiều tham số nhất (33.62M), chậm nhất (24.30 ms); (b) **Merged attention** — nối token hai modality thành chuỗi dài rồi self-attend, chuỗi dài → chi phí attention tăng bình phương; (c) **Ours — one-way** — chỉ chữ hỏi ảnh, đúng nhu cầu của MLM, rẻ nhất (6.42 ms).

- **Slide 14 — II. Proposed Method — Similarity Distribution Matching**
  - Dẫn: "Từ đây ta rời cấp token và quay về cấp vector toàn cục. Câu hỏi là: có hai vector rồi, ta dạy chúng nằm đúng chỗ bằng cách nào?"
  - **Mini-batch và ma trận tương đồng** — trong một mini-batch có $N$ cặp (ảnh, câu); tính cosine giữa **mọi** ảnh với **mọi** câu → **ma trận $N\times N$** (chính là hai lưới bên phải slide). Mỗi **hàng** = một ảnh so với tất cả các câu.
  - **$p$ — phân phối dự đoán** — lấy một hàng của ma trận similarity cho qua **softmax**: *"theo mô hình hiện tại, ảnh $i$ tin câu nào là của nó, với xác suất bao nhiêu"*.
  - **$\tau$ — temperature (nhiệt độ)** — chia similarity cho $\tau$ trước softmax. $\tau$ nhỏ → phân phối **nhọn**, chênh lệch nhỏ bị khuếch đại; $\tau$ lớn → phân phối **phẳng**. Ở đây $\tau=0.02$ tức nhân similarity với 50 — rất nhọn. **Hệ quả:** negative có similarity cao nhận xác suất lớn, tạo gradient mạnh → mô hình bị ép xử lý nó; đó là ý nghĩa của *emphasizes hard negatives*.
  - **Hard negative (mẫu âm khó)** — cặp ảnh–câu **không** đúng nhưng mô hình chấm điểm cao, ví dụ hai người khác nhau cùng mặc áo trắng quần đen. Đúng là trường hợp gây lỗi ở slide 4, nên xử lý được hard negative là xử lý đúng chỗ đau.
  - **$q$ — phân phối nhãn** — $y_{i,j}=1$ nếu ảnh $i$ và câu $j$ **cùng danh tính**, ngược lại 0; chuẩn hóa tổng bằng 1 nên nếu có $m$ câu cùng danh tính thì mỗi câu nhận $1/m$. **Điểm tinh tế:** nhãn dựa trên **danh tính**, không phải chỉ số cặp — nên nhiều ảnh/câu của cùng một người trong batch đều là positive. Đây là khác biệt so với InfoNCE của CLIP vốn chỉ coi đường chéo là đúng.
  - **KL divergence** — đo độ lệch giữa hai phân phối, bằng 0 khi trùng khớp; mục tiêu là kéo $p$ (mô hình đang nghĩ) về $q$ (sự thật).
  - **Bidirectional (hai chiều)** — $p^{i\to t}$ chuẩn hóa theo **hàng** (mỗi ảnh so mọi câu), $p^{t\to i}$ theo **cột** (mỗi câu so mọi ảnh); cộng cả hai để tối ưu cả hai chiều truy hồi, ràng buộc cho không gian nhúng chặt chẽ hơn.
  - **Ý nghĩa cốt lõi — câu cần chốt:** các loss ghép cặp thông thường chỉ quan tâm **"cặp đúng có điểm cao không"**; SDM quan tâm **"toàn bộ hình dạng phân phối có đúng không"** — vừa đẩy positive lên, vừa chủ động dìm negative đang nổi lên.
  - *(Code `compute_sdm`: `logit_scale = 1/temperature = 50`; `labels_distribute = labels / labels.sum(dim=1)`; KL tính theo chiều $\mathrm{KL}(p\Vert q)$ với `epsilon=1e-8` tránh log của 0.)*

- **Slide 15 — II. Proposed Method — Identity Classification Loss**
  - Dẫn: "SDM lo quan hệ **giữa** hai modality. Còn loss thứ ba này lo cấu trúc **bên trong** mỗi modality."
  - **ID loss / identity classification loss** — coi mỗi danh tính trong tập train là một **lớp** rồi bắt mô hình phân loại; CUHK-PEDES có 11.003 danh tính train → 11.003 lớp.
  - **$W$ — classifier tuyến tính dùng chung** — **cùng một** ma trận $W$ áp cho **cả** $f^v$ và $f^t$. Nếu dùng hai classifier riêng, mỗi modality sẽ tự hình thành hệ tọa độ riêng; dùng chung $W$ buộc cả hai tham chiếu **cùng một bộ tâm lớp** — một lực căn chỉnh gián tiếp bổ sung cho SDM.
  - **Class prototype (tâm lớp)** — mỗi hàng của $W$ là vector đại diện cho một danh tính; gradient kéo embedding về prototype đúng và đẩy khỏi prototype khác.
  - **Hệ số $\tfrac12$** — code tính CE trung bình trên batch cho từng modality rồi lấy trung bình hai giá trị *(`compute_id`)*.
  - **`identity-discriminative global clusters`** — ID loss dạy embedding của cùng một người **tụ thành cụm**, tách khỏi cụm người khác; tác động lên cấu trúc cụm, không trực tiếp lên thứ hạng truy hồi.
  - **`GRADIENT ROUTE`** — gradient cập nhật $W$ **và** cả hai CLIP encoder, **không** đi qua interaction encoder hay MLM head. Classifier bị **bỏ khi inference** (11.003 lớp chỉ có nghĩa trên tập train, tập test là người hoàn toàn khác).
  - **Điểm phải nói thẳng (ghi điểm phản biện):** ID loss là **auxiliary loss**, không phải đóng góp chính. Ablation ở slide 20 cho thấy dùng **một mình** nó làm **giảm** Rank-1 (CUHK 68.19 → 65.33; ICFG 56.74 → 53.38); chỉ có ích khi không gian đã được căn chỉnh tốt bởi SDM và IRR.

- **Slide 16 — II. Proposed Method — Training vs. Inference**
  - Dẫn: "Đây là slide mà em muốn khán giả nhớ nhất trong phần phương pháp, vì nó chính là luận điểm của cả bài báo."
  - **Tổng loss là PHÉP CỘNG, không phải trung bình cộng** — $\mathcal L = \mathcal L_{\mathrm{IRR}} + \mathcal L_{\mathrm{SDM}} + \mathcal L_{\mathrm{ID}}$ (Equation 7); code làm đúng vậy: `total_loss = sum([v for k, v in ret.items() if "loss" in k])`. Mặc định `loss_names='sdm+id+mlm'`, `mlm_loss_weight=1.0`, `id_loss_weight=1.0` — **không có trọng số nào khác 1**. Từng loss đã trung bình **bên trong** nó rồi (trên batch, trên các vị trí bị che) nên cộng ba scalar ở ngoài là hợp lý. *(Câu hay bị hỏi.)*
  - **Gradient được cộng tại các tham số dùng chung** — $\nabla_{\theta_v}\mathcal L = \nabla_{\theta_v}\mathcal L_{\mathrm{IRR}} + \nabla_{\theta_v}\mathcal L_{\mathrm{SDM}} + \nabla_{\theta_v}\mathcal L_{\mathrm{ID}}$; không backward ba lần với ba optimizer step mà autograd dựng **một** đồ thị chung, cộng ba scalar rồi backward **một lần**.
  - **Bảng định tuyến gradient** — image encoder và text encoder nhận gradient từ **cả ba** loss và **được giữ lại khi inference**; interaction encoder + MLM head (chỉ IRR), identity classifier $W$ (chỉ ID), temperature $\tau=0.02$ (cố định) — **đều bị bỏ**. Nghĩa là tri thức từ ba nhiệm vụ đã được **dồn vào đúng hai khối sống sót**.
  - **Vì sao bỏ nhánh phụ mà không mất kiến thức — lập luận quan trọng nhất:** interaction encoder và MLM head là một **giàn giáo huấn luyện**; nhiệm vụ của chúng là tạo gradient, gradient đó **đã** chảy vào hai encoder và **đã** thay đổi trọng số. Tháo giàn giáo đi thì trọng số đã thay đổi vẫn còn nguyên. Ẩn dụ: học sinh làm bài tập khó có hướng dẫn — đi thi không mang hướng dẫn theo, nhưng năng lực có được thì vẫn còn.
  - **Đóng góp về mặt hệ thống** — train nặng (hai encoder + interaction encoder + MLM head + classifier, câu chạy hai lượt), inference gọn (đúng hai encoder + một phép cosine). **So với CLIP dual encoder, chi phí inference không tăng chút nào** nhưng Rank-1 tăng 5–7 điểm. Lưu ý trung thực: bài báo **chưa** benchmark một vector database thật (chưa đo ANN index, footprint, latency end-to-end), dù kiến trúc hoàn toàn tương thích.

- **Slide 17 — III. Experiments — Three Benchmarks**
  - Dẫn: "Chuyển sang phần kiểm chứng. Bài báo đánh giá trên ba bộ dữ liệu, và mỗi bộ được chọn để kiểm tra một khía cạnh khác nhau."
  - **Số liệu ba bộ:** CUHK-PEDES — 13.003 danh tính / 40.206 ảnh / 80.412 mô tả, 2 mô tả/ảnh, benchmark **đầu tiên** của bài toán. ICFG-PEDES — 4.102 / 54.522 / 54.522, 1 mô tả/ảnh, **test gallery lớn** (19.848 cặp). RSTPReid — 4.101 / 20.505 / 41.010, 15 camera, 5 ảnh/danh tính, 2 mô tả/ảnh.
  - Split chi tiết (chỉ nói nếu được hỏi): CUHK train 11.003 danh tính / 34.054 ảnh / 68.108 mô tả, val và test mỗi tập 1.000 danh tính; ICFG train/test = 3.102 / 1.000 danh tính (34.674 / 19.848 cặp); RSTPReid train/val/test = 3.701 / 200 / 200.
  - **Identity-disjoint split — khái niệm quan trọng nhất của slide** — train và test **không chia sẻ bất kỳ danh tính nào**. **Vì sao quan trọng:** loại bỏ khả năng mô hình "học thuộc" danh tính; nó không thể ghi nhớ "người số 47 trông thế này" mà buộc phải học **cách ánh xạ thuộc tính ngôn ngữ sang đặc trưng thị giác** một cách tổng quát. Hệ quả: kết quả test đo đúng **khả năng khái quát hóa sang người chưa từng thấy**.
  - **Vì sao ba bộ chứ không phải một** — CUHK-PEDES là chuẩn so sánh lịch sử; ICFG-PEDES có gallery test lớn hơn nhiều nên kiểm tra khả năng chịu quy mô; RSTPReid 15 camera kiểm tra độ bền với thay đổi góc nhìn và điều kiện chụp.

- **Slide 18 — III. Experiments — Metrics and Training Setup**
  - Dẫn: "Ba chỉ số này đo ba thứ khác nhau, và khoảng cách giữa chúng sẽ nói lên điều thú vị ở slide hạn chế. Em xin giải thích bằng một ví dụ cụ thể."
  - **Ví dụ dùng chung cho cả ba chỉ số:** một truy vấn có **3 ảnh đúng** trong gallery, chúng nằm ở vị trí **1, 4 và 20**.
  - **Rank-k** — *có ít nhất một ảnh đúng trong Top-k hay không*, chỉ trả lời có/không. Ở ví dụ: Rank-1/5/10 đều **đạt**. Là chỉ số **thân thiện với người dùng nhất** (người dùng chỉ nhìn trang đầu), nhưng **bỏ qua** hai ảnh đúng còn lại.
  - **mAP (mean Average Precision)** — quan tâm **tất cả** ảnh đúng và vị trí của chúng; đẩy được cả ba lên cao thì mAP cao, nếu chỉ ảnh đầu đúng còn hai ảnh kia rất xa thì mAP thấp dù Rank-1 vẫn đạt. → **mAP luôn thấp hơn Rank-1 nhiều**, đừng để khán giả hiểu nhầm đó là mô hình kém.
  - **mINP (mean Inverse Negative Penalty)** — chỉ quan tâm **ảnh đúng nằm xa nhất** (vị trí 20 trong ví dụ), tức *phải duyệt bao xa mới gom đủ tất cả ảnh đúng*. **Khắc nghiệt nhất**, thường thấp hơn hẳn hai chỉ số kia. Ý nghĩa thực tế: ứng dụng cần **tìm đủ mọi lần xuất hiện** của một người (dựng lại lộ trình qua nhiều camera) thì mINP mới là chỉ số đáng quan tâm. ⚠️ mINP của IRRA trên ICFG chỉ **7.93** — con số này quay lại ở slide 22.
  - **Implementation — nói lướt, nhấn ba điểm:** $\tau=0.02$ **cố định**, không phải tham số học được; **learning rate phân tầng** — backbone CLIP pre-train dùng LR `1e−5` (nhỏ để không phá trọng số tốt sẵn có), module mới khởi tạo ngẫu nhiên (interaction encoder, MLM head, classifier) dùng `5e−5`, **gấp 5 lần** — thực hành chuẩn khi fine-tune; **một GPU RTX 3090 duy nhất** — quy mô một nhóm sinh viên tái lập được.
  - *(Bổ sung không có trên slide: augmentation gồm lật ngang, random crop có padding, random erasing; scheduler cosine decay; warm-up tuyến tính 5 epoch từ `1e−6`; repo chính thức chạy `batch_size = 64`.)*

- **Slide 19 — III. Results — State-of-the-Art Comparison (2023)**
  - Dẫn: "Slide này chỉ hiển thị Rank-1, vì đó là chỉ số dễ so sánh nhất. Số đầy đủ em để ở appendix."
  - **CLIP baseline** — chính CLIP ViT-B/16 fine-tune trực tiếp cho bài toán, **không có** IRR, **không có** SDM; là mốc đo xem đóng góp của bài báo đáng giá bao nhiêu. **CFine** — phương pháp tốt nhất trước đó. **IRRA** — mô hình đầy đủ.
  - **Quan sát 1 — IRRA thắng trên cả ba dataset.** Rank-1 đạt 73.38 / 63.46 / 60.20, so với CFine là **+3.81 / +2.63 / +9.65** điểm.
  - **Quan sát 2 — mức tăng trên RSTPReid lớn bất thường (+9.65).** Giải thích: RSTPReid là bộ multi-camera, biến thiên trong cùng danh tính lớn nhất — đúng trường hợp đặc trưng toàn cục thô dễ thất bại nhất và chi tiết cục bộ có giá trị nhất, nên IRR phát huy mạnh nhất.
  - **Quan sát 3 — thú vị nhất: CLIP baseline đã rất mạnh.** Trên RSTPReid đạt **54.05**, **cao hơn** CFine (50.55) dù CFine là công trình chuyên biệt. **Ý nghĩa:** ủng hộ lập luận ở slide 6 rằng pre-training **chung** trên cặp ảnh–văn bản có giá trị hơn ghép hai backbone pre-train **riêng** cho từng modality.
  - **Quan sát 4 — phép so sánh công bằng nhất là IRRA vs CLIP baseline**, vì cùng xuất phát điểm: **+5.19 / +6.72 / +6.15** điểm Rank-1. Đây mới đúng là phần đóng góp của IRR + SDM.
  - **Cách phát biểu chính xác về "SOTA":** nói **"đạt state of the art tại thời điểm công bố, so với các baseline được đánh giá trong bài báo"**; **đừng** nói "hiện nay vẫn là tốt nhất" — bài báo từ 2023, lĩnh vực thay đổi nhanh.
  - Số đầy đủ (chỉ khi được hỏi): CUHK 73.38 / 89.93 / 93.71 / 66.13 / 50.24; ICFG 63.46 / 80.25 / 85.82 / 38.06 / 7.93; RSTPReid 60.20 / 81.30 / 88.20 / 47.17 / 25.28 (R1/R5/R10/mAP/mINP).

- **Slide 20 — III. Results — Ablation: IRR and SDM**
  - Dẫn: "Ablation là phần em thấy trung thực nhất của bài báo, vì nó cũng cho thấy một thành phần **không** hiệu quả khi đứng một mình."
  - **Ablation study (nghiên cứu cắt bỏ)** — bật/tắt từng thành phần để đo đóng góp riêng; cách duy nhất phân biệt *"mô hình tốt"* với *"ý tưởng tốt"*.
  - **Mọi con số trên biểu đồ là mức TĂNG so với CLIP baseline**, không phải Rank-1 tuyệt đối — phải nói rõ, nếu không khán giả tưởng mô hình chỉ đạt 5 điểm.
  - **Takeaway 1 — `IRR > SDM`:** +3.04 / +4.22 / +3.85 so với +2.23 / +3.71 / +3.15, nhất quán trên cả ba dataset. **Ý nghĩa:** đóng góp mang tên bài báo (Implicit Relation Reasoning) đúng là đóng góp mạnh nhất — tên bài báo không bị "thổi".
  - **Takeaway 2 — `FULL MODEL WINS`, hai thành phần bổ sung cho nhau:** nếu chúng học cùng một thứ thì mô hình đầy đủ chỉ bằng thành phần mạnh nhất (~+4.22), thực tế đạt +6.72. **Ý nghĩa:** IRR và SDM học hai thứ **khác nhau** — IRR dạy mô hình *nhìn vào đâu*, SDM dạy mô hình *sắp xếp mọi thứ so với nhau*.
  - **Takeaway 3 — `ID LOSS — Alone, it may reduce R1`:** dùng một mình, Rank-1 **giảm** (CUHK 68.19 → **65.33**, ICFG 56.74 → **53.38**). **Vì sao:** ID loss tối ưu bài toán **phân loại**, không tối ưu **xếp hạng cross-modal** — nó gom cụm theo danh tính trong từng modality nhưng không đảm bảo cụm ảnh và cụm chữ của cùng một người trùng lên nhau; chỉ có ích khi đã có lực căn chỉnh khác (SDM, IRR). → **Đừng kể câu chuyện "mọi loss đều độc lập có lợi"**; nói thẳng điều này là điểm cộng khi phản biện.
  - **Takeaway 4 — `CMPM — Weaker than SDM`:** CMPM (Cross-Modal Projection Matching) là loss phổ biến trong các công trình trước; trong cấu hình CLIP này CMPM trên CUHK chỉ đạt **59.31** còn SDM đạt **70.42**. **Ý nghĩa:** bằng chứng trực tiếp cho động cơ thiết kế SDM — không phải "thay loss cho khác người" mà vì loss cũ thực sự kém trong cấu hình này.

- **Slide 21 — III. Results — Efficiency and Qualitative Results**
  - Dẫn: "Slide này có hai nửa: nửa trên trả lời *có đắt không*, nửa dưới trả lời *tốt hơn ở chỗ nào*."
  - **Nửa trên — hiệu quả tính toán (Table 5, CUHK-PEDES):** Co-attention 33.62M / 24.30 ms / 73.28; Merged attention 12.61M / 19.20 ms / 73.21; **IRRA (one-way) 13.66M / 6.42 ms / 73.38**.
    - **Rank-1 của ba module gần như bằng nhau** (73.21–73.38) → *kiểu* module tương tác không quan trọng lắm, quan trọng là **có** tương tác.
    - **Nhưng chi phí chênh lệch rất lớn** — IRRA nhanh hơn merged attention ~3 lần, nhanh hơn co-attention ~3,8 lần, với số tham số gần bằng merged attention.
    - → **Kết luận thiết kế:** chọn module rẻ nhất là lựa chọn đúng vì không mất gì về độ chính xác.
  - **Cảnh báo để tránh bị vặn:** bài báo **không mô tả đầy đủ giao thức đo thời gian** ở Table 5 — phải hiểu đây là **so sánh nội bộ giữa ba module trong cùng điều kiện**, không phải latency end-to-end của hệ thống production.
  - **Điều dễ gây hiểu nhầm, phải nói rõ:** 6.42 ms là chi phí **trong lúc huấn luyện**; khi inference module này **bị bỏ hoàn toàn** nên chi phí thực tế khi truy hồi là **0** — đó là điều nhãn đỏ trên slide muốn nói.
  - **Nửa dưới — kết quả định tính (Figure 5):** mỗi truy vấn hai hàng, trên là baseline dưới là IRRA; khung **xanh** = đúng, khung **đỏ** = sai; các cụm **tô cam** trong câu truy vấn là thuộc tính phân biệt (*green pants*, *black book bag*, *blue tennis shoes*). **Cách đọc:** IRRA đưa nhiều ảnh đúng lên Top-10 hơn, và các ảnh nó chọn thường khớp chính xác ở những cụm tô cam — đúng những chi tiết nhỏ mà slide 4 nêu là nguồn gốc khó khăn và slide 12 nêu là mục tiêu của IRR. → **Bằng chứng định tính** cho cơ chế, bổ sung cho bằng chứng định lượng ở slide 19–20.

- **Slide 22 — IV. Discussion — Limitations and Critical Analysis**
  - Dẫn: "Em xin tách rõ: hạn chế số một là do chính tác giả nêu, còn ba hạn chế sau là đánh giá thêm của em sau khi đọc kỹ bảng số liệu và mã nguồn." (Dòng phân định này quan trọng — cho thấy đọc có phê phán chứ không chép lại phần Conclusion.)
  - **1. Phrase-level semantics — hạn chế tác giả thừa nhận:** IRRA chỉ mask **từng token đơn, ngẫu nhiên** nên giỏi ngữ nghĩa **cấp từ** nhưng có thể yếu ở **cấp cụm từ**. Ví dụ *"black book bag"* không đơn thuần là tổng của *black* + *book* + *bag*; che riêng *book* thì mô hình vẫn đoán được nhờ ngữ cảnh chữ mà không thực sự hiểu cụm. **Hướng khắc phục:** *span masking* / *phrase masking* — che cả cụm cùng lúc, buộc mô hình dùng ảnh thay vì dựa vào từ lân cận.
  - **2. Hard positives — quan sát từ số liệu:** mINP trên ICFG chỉ **7.93** trong khi Rank-1 là 63.46 — khoảng cách rất lớn. **Ý nghĩa:** mô hình rất giỏi đưa **một** ảnh đúng lên đầu nhưng rất yếu trong việc gom **đủ tất cả** ảnh đúng; những ảnh đúng khó (góc lạ, bị che) vẫn nằm rất xa. **Hệ quả thực tế:** cần "tìm ra người này ở đâu đó" thì IRRA rất tốt; cần "tìm **mọi** lần người này xuất hiện" (dựng lộ trình qua nhiều camera) thì còn xa mới dùng được. Đây là lý do cài sẵn khái niệm mINP ở slide 18.
  - **3. Generalization — thiếu bằng chứng:** mọi thí nghiệm đều **within-dataset**; không có **cross-dataset** (train CUHK, test ICFG) nên chưa biết chịu được domain shift đến đâu; mọi mô tả đều **tiếng Anh** nên chưa biết gì về đa ngôn ngữ (rất thực tế với ứng dụng ở Việt Nam); chưa đánh giá trên camera mới hoặc điều kiện mới.
  - **4. Deployment and ethics — hai nhóm riêng biệt, tách rõ khi nói:**
    - **Triển khai:** tuyên bố inference hiệu quả nhưng chưa đo chỉ mục ANN, chưa đo footprint bộ nhớ của gallery, chưa đo latency end-to-end — với học phần CSDL thì đây đúng là phần còn thiếu.
    - **Đạo đức:** person search là công nghệ **lưỡng dụng**; nói ngắn nhưng nghiêm túc — **riêng tư** (tìm một người chỉ bằng lời mô tả → cần kiểm soát mục đích, phân quyền, lưu vết truy vấn); **thiên lệch** (mô tả ngôn ngữ tự nhiên có thể mang định kiến; bài báo không đánh giá hiệu năng theo nhóm nhân khẩu học); **giám sát** (cần khung pháp lý đi kèm, không chỉ là bài toán kỹ thuật).

- **Slide 23 — Three Key Takeaways**
  - Dẫn: "Em xin tóm lại ba điều."
  - **Takeaway 1 — Local relation learning during training; global embeddings at inference** — **luận điểm trung tâm**, nối slide 4 (mâu thuẫn) với slide 16 (cách hóa giải).
  - **Takeaway 2 — IRR + SDM** — hai đóng góp kỹ thuật, nối slide 12–14 (cơ chế) với slide 20 (ablation chứng minh cả hai đều cần).
  - **Takeaway 3 — SOTA at CVPR 2023** — bằng chứng, nối slide 19; giữ đúng cách phát biểu *tại thời điểm công bố*.
  - **Bốn hướng mở rộng — mỗi hướng ứng đúng một hạn chế ở slide 22:** **Phrase masking** → (1) ngữ nghĩa cấp cụm từ; **Hard-sample mining** (tăng mINP) → (2) hard positives; **Multilingual retrieval** (truy vấn tiếng Việt) → (3) khả năng tổng quát hóa; **Vector databases** (tích hợp FAISS/HNSW, đo latency và recall thật) → (4) triển khai. Chỉ ra được tương ứng một-một này khiến phần kết luận nghe rất chặt chẽ, và cũng là gợi ý tự nhiên cho đồ án cuối kỳ.

- **Slide A1 — Appendix A: SDM vs. InfoNCE and CMPM** *(dự phòng, dùng khi bị hỏi "SDM khác gì các loss contrastive đã có")*
  - **InfoNCE** (loss gốc của CLIP) — tín hiệu chính là cặp đúng trên đường chéo đối lập với mọi cặp sai trong batch; giả định **đúng một** positive mỗi hàng. Baseline CLIP dùng loss này đã rất mạnh.
  - **CMPM** — cross-modal projection matching, dùng độ dài hình chiếu; độ dài hình chiếu hoạt động như một scale biến thiên, khó kiểm soát độ nhọn của phân phối — trong cấu hình CLIP chỉ đạt 59.31 trên CUHK.
  - **SDM** — KL giữa phân phối similarity và phân phối nhãn theo danh tính; temperature **cố định** τ=0.02, hỗ trợ **nhiều** positive cùng danh tính, đạt 70.42 trên CUHK.
  - **Câu trả lời một câu:** "SDM biến toàn bộ hàng và cột của ma trận similarity thành phân phối xác suất và buộc nó khớp phân phối nhãn, thay vì chỉ tối ưu một cặp dương trên đường chéo."

- **Slide A2 — Appendix B: Complete Results** *(dự phòng)*
  - Bảng đầy đủ R1/R5/R10/mAP/mINP: CUHK-PEDES 73.38 / 89.93 / 93.71 / 66.13 / 50.24; ICFG-PEDES 63.46 / 80.25 / 85.82 / 38.06 / 7.93; RSTPReid 60.20 / 81.30 / 88.20 / 47.17 / 25.28.
  - **Sai khác số liệu trong bản arXiv v1** (chỉ nói nếu bị chất vấn): đoạn văn trang 7 viết CLIP baseline trên CUHK "Rank-1 và mAP đạt 68.19% và 86.47%" — thực ra `86.47` là **Rank-5**, mAP trong Table 1 là `61.12`. Table 1 ghi IRRA Rank-5 trên CUHK là `89.93` còn Table 4 ghi `89.83` → dùng `89.93` theo README. ICFG có sai khác làm tròn nhỏ (`80.24/80.25`, `38.05/38.06`, `7.92/7.93`) → dùng số trong Table 2 của bản PDF. Phần ablation viết SDM hơn CMPM `2.2` điểm trên RSTPReid nhưng Table 4 cho `57.20 − 55.40 = 1.80` → **khi trình bày dùng số gốc trong bảng**.
  - **Cách phát biểu an toàn về SOTA:** "State of the art tại thời điểm công bố, so với các baseline được đánh giá trong bài báo."

- **Slide A3 — Appendix C: Frequently Asked Questions** *(dự phòng)*
  - Nội dung nằm ở ngân hàng câu hỏi Q&A, đầy đủ hơn phần trên slide.
