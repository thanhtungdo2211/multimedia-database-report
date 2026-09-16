# Speaker notes — IRRA (bản bám sát deck `slide/IRRA_multimedia_database.pptx`)

> **Bài báo:** *Cross-Modal Implicit Relation Reasoning and Aligning for Text-to-Image Person Retrieval* — Ding Jiang, Mang Ye, CVPR 2023, tr. 2787–2797
> **Deck:** 23 slide trình bày + 3 slide appendix (tổng 26 slide vật lý)
> **Thời lượng mục tiêu:** ~20–23 phút cho phần trình bày, còn lại dành cho Q&A
> **Mã nguồn đối chiếu:** [`../IRRA/`](../IRRA/) — mọi con số kỹ thuật trong file này đã được kiểm tra lại trực tiếp trong code.

---

## Cách dùng tài liệu này

Mỗi slide được trình bày theo đúng 6 mục, luôn cùng thứ tự:

| Mục | Dùng để làm gì |
|---|---|
| **A. Trên slide có gì** | Liệt kê đúng những gì khán giả đang nhìn thấy, để bạn biết mình đang chỉ vào đâu |
| **B. Dẫn vào slide** | 1–2 câu nối từ slide trước sang slide này — đây là phần giữ mạch câu chuyện |
| **C. Giải thích từng khái niệm** | Từng thuật ngữ trên slide được định nghĩa tường minh, không bỏ sót chữ nào |
| **D. Slide này giải quyết vấn đề gì** | Vai trò của slide trong toàn bộ lập luận: nó trả lời câu hỏi nào |
| **E. Lời thuyết trình** | Đoạn nói liền mạch, có thể đọc gần như nguyên văn |
| **F. Câu chuyển** | Câu cuối cùng để mở sang slide sau |
| **G. Nếu bị hỏi** | (chỉ ở các slide dễ bị vặn) câu trả lời ngắn, chính xác |

Không có Mermaid trong tài liệu này. Các hình cần dán vào slide đều là hình có sẵn trong bài báo hoặc hình bạn đã dựng trong `slide/presentation.drawio`.

---

## Mạch kể chuyện toàn bài — học thuộc 7 câu này

Nếu quên hết mọi thứ khác, chỉ cần giữ được 7 câu sau là bài nói vẫn có mạch:

1. **Nhu cầu.** Ta cần tìm một người trong kho ảnh lớn, nhưng trong tay chỉ có một câu mô tả, không có ảnh truy vấn.
2. **Nút thắt.** Ảnh và ngôn ngữ là hai loại dữ liệu khác hẳn nhau, mà thứ phân biệt hai người lại nằm ở chi tiết rất nhỏ: màu áo, chiếc túi, đôi giày.
3. **Giới hạn cách cũ.** Khớp toàn cục thì nhanh nhưng bỏ sót chi tiết; khớp từng bộ phận thì bắt được chi tiết nhưng tốn kém và dễ nhiễu.
4. **Ý tưởng chính.** IRRA bắt ảnh và câu "nói chuyện" ở mức token **trong lúc huấn luyện** bằng bài toán điền từ bị che, nhưng **khi truy hồi vẫn chỉ so một vector với một vector**.
5. **Mảnh ghép thứ hai.** SDM thay loss ghép cặp thông thường, khớp cả **hình dạng phân phối** độ tương đồng với phân phối nhãn.
6. **Bằng chứng.** Tốt nhất tại thời điểm công bố trên cả ba benchmark; ablation cho thấy IRR và SDM đều đóng góp và bổ sung cho nhau.
7. **Đánh giá.** Thực dụng và hiệu quả, nhưng còn hở ở ngữ nghĩa cấp cụm từ, hard positive, khả năng tổng quát hóa và khía cạnh riêng tư.

**Một câu tóm tắt cả bài báo, dùng khi bị hỏi "nói ngắn gọn IRRA làm gì":**
> "IRRA đưa chi tiết vào **quá trình học**, nhưng không đưa chi phí của chi tiết đó vào **quá trình truy hồi**."

---

## Bản đồ deck

| Slide | Tiêu đề trên slide | Phần | Thời lượng |
|---:|---|---|---:|
| 1 | Title | — | 25 s |
| 2 | I. Introduction — From Description to Top-k | Dẫn nhập | 60 s |
| 3 | I. Introduction — Multimedia Database Perspective | Dẫn nhập | 65 s |
| 4 | I. Introduction — Why Is the Task Difficult? | Dẫn nhập | 70 s |
| 5 | I. Background — Three Matching Paradigms | Nền tảng | 80 s |
| 6 | I. Background — Dual-Stream Models and CLIP | Nền tảng | 70 s |
| 7 | II. Proposed Method — Research Question | Phương pháp | 55 s |
| 8 | II. Proposed Method — IRRA Overview | Phương pháp | 90 s |
| 9 | II. Proposed Method — CLIP Dual Encoder | Phương pháp | 65 s |
| 10 | II. Proposed Method — Inside the ViT Image Encoder | Phương pháp | 80 s |
| 11 | II. Proposed Method — Inside the CLIP Text Encoder | Phương pháp | 75 s |
| 12 | II. Proposed Method — IRR through MLM | Phương pháp | 85 s |
| 13 | II. Proposed Method — Multimodal Interaction | Phương pháp | 80 s |
| 14 | II. Proposed Method — Similarity Distribution Matching | Phương pháp | 85 s |
| 15 | II. Proposed Method — Identity Classification Loss | Phương pháp | 60 s |
| 16 | II. Proposed Method — Training vs. Inference | Phương pháp | 75 s |
| 17 | III. Experiments — Three Benchmarks | Thực nghiệm | 60 s |
| 18 | III. Experiments — Metrics and Training Setup | Thực nghiệm | 75 s |
| 19 | III. Results — State-of-the-Art Comparison | Kết quả | 80 s |
| 20 | III. Results — Ablation: IRR and SDM | Kết quả | 85 s |
| 21 | III. Results — Efficiency and Qualitative Results | Kết quả | 75 s |
| 22 | IV. Discussion — Limitations and Critical Analysis | Thảo luận | 85 s |
| 23 | Three Key Takeaways | Kết luận | 60 s |
| A1–A3 | Appendix A / B / C | Dự phòng | không trình bày |

Tổng phần chính: **khoảng 21 phút**.

---

# PHẦN MỞ ĐẦU

---

## Slide 1 — Title

**Thời lượng:** ~25 giây

### A. Trên slide có gì

- Logo HUST, thẻ đỏ `MULTIMEDIA DATABASE`
- Tên bài báo ba dòng: *Cross-Modal Implicit Relation Reasoning and Aligning for Text-to-Image Person Retrieval*
- `IRRA • CVPR 2023`, tác giả `Ding Jiang, Mang Ye`
- Dòng người trình bày và `Hanoi, 2026`

### B. Dẫn vào slide

Không cần dẫn — đây là câu mở đầu buổi nói.

### C. Giải thích từng khái niệm

Bạn **chưa** cần giải thích gì ở slide này, nhưng nên đọc đúng và giải nghĩa nhanh hai cụm trong tên bài:

- **Text-to-Image Person Retrieval** — truy hồi ảnh người từ mô tả văn bản. Đầu vào là một câu, đầu ra là ảnh.
- **Implicit Relation Reasoning** — suy luận quan hệ ẩn. "Ẩn" ở đây là điểm mấu chốt của cả bài báo, và bạn sẽ giải thích kỹ ở slide 7.
- **IRRA** — viết tắt của chính tên phương pháp: **I**mplicit **R**elation **R**easoning and **A**ligning.

### D. Slide này giải quyết vấn đề gì

Đặt kỳ vọng. Trong 25 giây bạn phải làm khán giả hiểu bài báo này **cân bằng giữa độ chính xác và chi phí truy hồi** — đó là sợi chỉ xuyên suốt toàn bộ bài nói.

### E. Lời thuyết trình

> "Em xin phép bắt đầu. Hôm nay em trình bày IRRA — viết tắt của Implicit Relation Reasoning and Aligning — một phương pháp truy hồi ảnh người bằng mô tả ngôn ngữ tự nhiên, công bố tại CVPR 2023 bởi Ding Jiang và Mang Ye.
>
> Điểm mà em thấy đáng chú ý nhất, và cũng là thứ em sẽ quay lại nhiều lần trong bài, là: mô hình học tương tác giữa ảnh và văn bản ở mức rất chi tiết **trong quá trình huấn luyện**, nhưng khi triển khai thì vẫn chỉ so sánh một vector ảnh với một vector văn bản. Đây là một cân bằng rất đẹp giữa độ chính xác và chi phí truy hồi — và cũng chính là lý do bài báo này phù hợp với học phần Cơ sở dữ liệu đa phương tiện."

### F. Câu chuyển

> "Trước khi xem kiến trúc, em xin bắt đầu từ một tình huống rất đời thường."

---

## Slide 2 — I. Introduction — From Description to Top-k

**Thời lượng:** ~60 giây

### A. Trên slide có gì

- **Cột trái:** thẻ `TEXT QUERY` với câu ví dụ *"A man wearing a white-and-gray striped shirt, green pants, and shoes."*, bên dưới là hai ô `INPUT — Natural-language description` và `OUTPUT — Ranked image list`
- **Mũi tên chevron** sang phải
- **Cột phải:** hai dải kết quả xếp chồng, nhãn `Baseline` ở trên và `IRRA` ở dưới (trích Figure 5 của bài báo)
- **Thanh dưới cùng:** `Cross-modal retrieval` — `query = text → gallery = images → retrieve Top-k`

### B. Dẫn vào slide

> "Hãy tưởng tượng một nhân viên an ninh cần tìm một người trong kho camera, nhưng trong tay không hề có ảnh của người đó — chỉ có lời kể của nhân chứng."

### C. Giải thích từng khái niệm

- **Query (truy vấn)** — thứ người dùng đưa vào. Ở đây query **không phải là ảnh** mà là một câu tiếng Anh tự do. Đây chính là điểm khác biệt so với Re-ID truyền thống.
- **Gallery** — kho ảnh cần tìm kiếm trong đó. Trong các benchmark của bài báo, gallery có từ vài nghìn đến gần hai mươi nghìn ảnh.
- **Ranked image list (Top-k)** — đầu ra **không phải một đáp án duy nhất** mà là một danh sách ảnh đã sắp xếp theo mức độ phù hợp giảm dần. Người dùng nhìn 10 ảnh đầu và tự chọn.
- **Cross-modal retrieval** — truy hồi liên phương thức: truy vấn thuộc một modality (văn bản), kết quả thuộc modality khác (ảnh). Đây là điểm khiến bài toán khó hơn tìm kiếm ảnh-bằng-ảnh.
- **Person Re-ID (nhắc để đối chiếu, không có trên slide)** — bài toán truyền thống: đưa vào một **ảnh** người, tìm các ảnh cùng người đó ở camera khác. Nếu có ảnh truy vấn thì dùng Re-ID; bài toán hôm nay là khi **không có** ảnh đó.
- **Hai dải Baseline / IRRA** — hai kết quả cho *cùng một câu truy vấn*. Bạn chỉ cần nói: hàng dưới có nhiều ảnh đúng được đẩy lên cao hơn. Chưa cần giải thích vì sao — đó là việc của phần sau.

### D. Slide này giải quyết vấn đề gì

Slide này **định nghĩa bài toán**. Nó trả lời đúng một câu hỏi: *đầu vào là gì, đầu ra là gì?* Khán giả phải rời slide này với hình dung rất cụ thể: một câu chữ đi vào, một danh sách ảnh đi ra.

Nó cũng gieo trước điều sẽ chứng minh ở cuối bài: hai dải ảnh Baseline và IRRA cho thấy có chỗ để cải thiện.

### E. Lời thuyết trình

> "Nếu ta có sẵn một ảnh khuôn mặt hoặc ảnh toàn thân, ta có thể dùng person Re-ID truyền thống. Nhưng trong rất nhiều tình huống, người dùng chỉ nhớ bằng lời: màu áo, kiểu quần, chiếc túi hay đôi giày. Ví dụ đúng như câu trên slide — *một người đàn ông mặc áo sọc trắng xám, quần xanh lá và đi giày*.
>
> Nhiệm vụ của hệ thống là biến câu đó thành một truy vấn, rồi xếp hạng hàng nghìn ảnh trong gallery. Có hai điều cần lưu ý ở đây.
>
> Thứ nhất, đầu ra không phải một nhãn đúng duy nhất như bài toán phân loại, mà là một **danh sách xếp hạng** — Top-k. Cùng một người có thể xuất hiện ở nhiều camera, nhiều góc nhìn, nhiều thời điểm, nên có thể có nhiều ảnh đúng cùng lúc.
>
> Thứ hai, truy vấn và kết quả thuộc hai loại dữ liệu khác nhau. Đây gọi là **cross-modal retrieval**, và chính sự khác nhau về bản chất dữ liệu này là nguồn gốc của mọi khó khăn ta sẽ bàn ở các slide sau.
>
> Ở bên phải slide, em để sẵn kết quả của baseline và của IRRA cho cùng một câu truy vấn. Em sẽ quay lại hình này ở phần kết quả."

### F. Câu chuyển

> "Về bản chất cơ sở dữ liệu, câu hỏi này được biến thành một phép tìm kiếm lân cận trong không gian vector. Ta xem pipeline đó."

---

## Slide 3 — I. Introduction — Multimedia Database Perspective

**Thời lượng:** ~65 giây

### A. Trên slide có gì

- Thẻ `OFFLINE • GALLERY INDEXING` + sơ đồ pipeline offline
- Thẻ `ONLINE • QUERY PROCESSING` + sơ đồ pipeline online

### B. Dẫn vào slide

> "Đây là slide gắn bài báo với học phần của chúng ta. Một hệ thống truy hồi đa phương tiện luôn có hai pha, và bài báo chỉ can thiệp vào đúng một trong hai."

### C. Giải thích từng khái niệm

- **Pha offline — lập chỉ mục gallery.** Toàn bộ ảnh trong kho được đưa qua image encoder **một lần duy nhất**, mỗi ảnh biến thành một vector cố định (ở đây là 512 chiều). Các vector này được lưu lại, có thể xây chỉ mục lên trên. Pha này chạy trước, không liên quan đến người dùng.
- **Embedding / feature vector** — biểu diễn số của một đối tượng đa phương tiện. Toàn bộ ý nghĩa của tấm ảnh bị nén vào một dãy số. Chất lượng của hệ thống phụ thuộc hoàn toàn vào việc dãy số này có "đúng" hay không.
- **Pha online — xử lý truy vấn.** Câu mô tả của người dùng được mã hóa **một lần**, thành một vector cùng số chiều, cùng không gian. Sau đó tính độ tương đồng với toàn bộ vector ảnh đã lưu và trả về Top-k.
- **Cosine similarity** — độ đo dùng để so hai vector:

  $$\operatorname{sim}(f^v,f^t)=\frac{(f^v)^\top f^t}{\lVert f^v\rVert\;\lVert f^t\rVert}$$

  Nó đo **góc** giữa hai vector, không đo độ dài. Giá trị trong khoảng −1 đến 1, càng gần 1 càng giống nhau. Vì đã chuẩn hóa độ dài nên nó bền với việc encoder xuất ra vector có norm khác nhau.
- **Joint embedding space (không gian nhúng chung)** — điều kiện tiên quyết để phép cosine ở trên có nghĩa: vector ảnh và vector chữ phải nằm trong **cùng một không gian**. Nếu không, so sánh chúng là vô nghĩa. Toàn bộ việc huấn luyện trong bài báo chính là để tạo ra không gian chung này.
- **Chỉ mục vector / ANN (nhắc thêm)** — HNSW, IVF, FAISS… là các cấu trúc dữ liệu giúp không phải quét tuyến tính toàn bộ gallery. **Bài báo không nghiên cứu phần này.**

### D. Slide này giải quyết vấn đề gì

Slide này làm hai việc:

1. **Định vị đóng góp của bài báo.** Trong toàn bộ pipeline trên, IRRA chỉ cải tiến **hai khối encoder**. Nó không đụng đến thuật toán chỉ mục, không đụng đến cách lưu trữ. Nói rõ điều này giúp bạn tránh bị hỏi vặn "vậy tăng tốc ở đâu".
2. **Giải thích vì sao kiến trúc dual-stream là bắt buộc với cơ sở dữ liệu.** Vì gallery được mã hóa trước, chi phí online chỉ còn một lần encode câu truy vấn cộng phép nhân ma trận. Nếu mô hình bắt buộc phải xử lý **từng cặp** ảnh–câu cùng lúc thì mọi thứ sụp đổ ở quy mô gallery lớn — và đó chính là lý do slide 6 tồn tại.

### E. Lời thuyết trình

> "Nhìn dưới góc độ cơ sở dữ liệu đa phương tiện, hệ thống này có hai pha rõ rệt.
>
> Ở **pha offline**, ta mã hóa trước toàn bộ gallery. Mỗi ảnh đi qua image encoder đúng một lần và trở thành một vector 512 chiều. Ta lưu các vector này lại và có thể xây chỉ mục lên trên.
>
> Ở **pha online**, khi người dùng gõ một câu, ta mã hóa câu đó đúng một lần, rồi tính cosine similarity với toàn bộ vector ảnh đã có sẵn và trả về Top-k. Cosine similarity đo góc giữa hai vector, nên nó không quan tâm độ dài vector, chỉ quan tâm hướng.
>
> Điều kiện để phép so sánh này có nghĩa là hai vector phải nằm trong **cùng một không gian nhúng**. Đây chính là thứ khó nhất và cũng là thứ mà toàn bộ phần huấn luyện của bài báo nhắm tới.
>
> Em muốn nói rõ một điểm để tránh hiểu nhầm: bài báo **không** nghiên cứu thuật toán chỉ mục gần đúng như HNSW hay IVF. Đóng góp của họ nằm hoàn toàn ở việc học hai encoder sao cho khoảng cách vector thực sự phản ánh đúng danh tính và đúng mô tả. Nhưng chính vì thiết kế cho phép mã hóa gallery trước, kiến trúc này rất hợp với mô hình cơ sở dữ liệu vector — và đó là điểm em sẽ nhấn lại ở slide Train và Inference."

### F. Câu chuyển

> "Pipeline nghe thì đơn giản, nhưng học ra được một không gian chung đáng tin cậy lại rất khó. Vì sao?"

### G. Nếu bị hỏi

**"Vậy bài báo có làm hệ thống truy hồi nhanh hơn không?"**
> Không nhanh hơn CLIP dual encoder — nó **bằng** CLIP dual encoder về chi phí inference, trong khi chính xác hơn đáng kể. Cái nhanh hơn là so với nhóm phương pháp explicit local matching, vốn phải lưu và so nhiều vector cục bộ cho mỗi ảnh.

---

## Slide 4 — I. Introduction — Why Is the Task Difficult?

**Thời lượng:** ~70 giây

### A. Trên slide có gì

Bốn thẻ đánh số 2×2:

1. `Large intra-identity variation` — *Viewpoint • pose • lighting • occlusion*
2. `Modality heterogeneity` — *Pixels/patches ↔ tokens and word order*
3. `Subtle discriminative details` — *White/black bag • striped/plain shirt • shoes*
4. `Language ambiguity` — *Arbitrary order • missing attributes • synonyms*

Dòng chốt dưới cùng: *Learn fine-grained local cues while retaining efficient global retrieval.*

### B. Dẫn vào slide

> "Có bốn khó khăn, và em muốn khán giả để ý rằng hai khó khăn đầu đến từ **dữ liệu**, còn hai khó khăn sau đến từ **ngữ nghĩa**."

### C. Giải thích từng khái niệm

- **Intra-identity variation (biến thiên trong cùng một danh tính)** — cùng một người, nhưng hai tấm ảnh có thể trông rất khác nhau. Nguyên nhân: *viewpoint* (camera chụp từ trước hay sau lưng), *pose* (đang đứng hay đang bước), *lighting* (trong nhà, ngoài nắng), *occlusion* (bị người khác hoặc vật thể che khuất). Hệ quả: mô hình không thể chỉ học "trông giống nhau thì là một người".
- **Modality heterogeneity (không đồng nhất giữa hai phương thức)** — ảnh là tín hiệu **liên tục, hai chiều, không có thứ tự tự nhiên**; câu là chuỗi **ký hiệu rời rạc, một chiều, thứ tự mang nghĩa**. Hai cấu trúc này không có cách ghép trực tiếp; buộc phải học một ánh xạ về không gian chung.
- **Subtle discriminative details (chi tiết phân biệt rất nhỏ)** — đây là điểm **quan trọng nhất của slide**. Trong tập dữ liệu, rất nhiều người có mô tả toàn cục gần như giống hệt nhau: đều là "người phụ nữ mặc áo sáng màu, quần tối màu". Thứ duy nhất phân biệt họ là chi tiết: túi **trắng** hay túi **đen**, áo **sọc** hay áo **trơn**. Một biểu diễn toàn cục thô sẽ làm nhòe đúng những chi tiết này.
- **Language ambiguity (mơ hồ của ngôn ngữ)** — hai người khác nhau mô tả cùng một bức ảnh sẽ viết khác nhau: thứ tự thuộc tính tùy ý ("áo trắng quần đen" hay "quần đen áo trắng"), có thể bỏ sót thuộc tính, và dùng từ đồng nghĩa ("purse" / "handbag" / "bag").
- **Dòng chốt** — *học được manh mối cục bộ chi tiết, nhưng vẫn giữ được truy hồi toàn cục hiệu quả*. Đây chính là **mâu thuẫn trung tâm** mà IRRA sẽ giải quyết. Hãy dừng lại và nhấn vào câu này.

### D. Slide này giải quyết vấn đề gì

Slide này **tạo ra sự căng thẳng** cho cả bài nói. Nó dựng lên một mâu thuẫn tưởng như không thể hòa giải:

- Muốn phân biệt đúng người → cần **chi tiết cục bộ**
- Muốn truy hồi nhanh trên gallery lớn → cần **một vector toàn cục duy nhất**

Nếu khán giả cảm nhận được mâu thuẫn này, thì toàn bộ phần phương pháp phía sau sẽ trở nên hiển nhiên là cần thiết. Nếu không, phần phương pháp sẽ nghe như một chuỗi kỹ thuật rời rạc.

### E. Lời thuyết trình

> "Bài toán này khó vì bốn lý do, và em xin chia chúng thành hai nhóm.
>
> **Hai lý do đầu đến từ bản chất dữ liệu.** Thứ nhất là *intra-identity variation*: cùng một người nhưng ảnh có thể rất khác do góc nhìn, dáng đi, ánh sáng hay bị che khuất. Thứ hai là *modality heterogeneity*: một bên là tín hiệu thị giác liên tục, bên kia là chuỗi ký hiệu rời rạc có thứ tự. Hai cấu trúc này không ghép trực tiếp được với nhau.
>
> **Hai lý do sau đến từ ngữ nghĩa, và em cho rằng chúng nặng hơn.** Trong các tập dữ liệu, rất nhiều người có mô tả toàn cục gần như giống hệt nhau. Mô hình chỉ có thể phân biệt bằng những chi tiết rất nhỏ: túi trắng hay túi đen, áo sọc hay áo trơn. Nhưng cùng lúc đó, ngôn ngữ lại mơ hồ: mỗi người mô tả theo một thứ tự khác nhau, có thể bỏ sót thuộc tính, và dùng từ đồng nghĩa.
>
> Gộp lại, ta có một mâu thuẫn rất rõ, chính là dòng chốt ở cuối slide. Để **không nhầm người**, ta cần biểu diễn được chi tiết cục bộ. Để **tìm nhanh trong gallery lớn**, ta lại cần một vector toàn cục duy nhất. Hai yêu cầu này kéo về hai hướng ngược nhau — và toàn bộ phần còn lại của bài trình bày là câu trả lời cho việc làm sao dung hòa chúng."

### F. Câu chuyển

> "Các công trình trước IRRA đã lần lượt thử cả hai cực của mâu thuẫn này."

---

## Slide 5 — I. Background — Three Matching Paradigms

**Thời lượng:** ~80 giây

### A. Trên slide có gì

Ba thẻ xếp dọc bên trái:

| Thẻ | Mô tả | Đánh giá |
|---|---|---|
| `GLOBAL` | One image vector ↔ one text vector | Fast, but misses fine details |
| `EXPLICIT LOCAL` | Body parts ↔ textual phrases | Noisy priors; multiple vectors to store and compare |
| `IRRA` | Implicit local learning during training | Global embeddings at inference |

Bên phải: **Figure 1** của bài báo, minh họa ba paradigm (a), (b), (c).

### B. Dẫn vào slide

> "Slide trước kết thúc bằng một mâu thuẫn. Slide này cho thấy hai cách giải quyết đã có, và vì sao cả hai đều chưa đủ."

### C. Giải thích từng khái niệm

**1. Global matching**
- Cách làm: nén cả tấm ảnh thành một vector, nén cả câu thành một vector, rồi đặt loss ở cuối mạng để kéo hai vector của cặp đúng lại gần nhau.
- Ưu: cực kỳ nhanh khi truy hồi, và đúng với mô hình cơ sở dữ liệu đã nói ở slide 3.
- Nhược: loss chỉ đặt ở **đầu ra cuối cùng**. Hai luồng ảnh và chữ không hề trao đổi thông tin ở các tầng giữa. Nên chi tiết cục bộ dễ bị "trung bình hóa" và biến mất.

**2. Explicit local matching**
- Cách làm: tách ảnh thành các vùng — đầu, thân, chân — hoặc các vùng thuộc tính; tách câu thành các cụm từ; rồi ghép từng vùng với từng cụm.
- **Prior (tri thức tiên nghiệm)** — thường là một mô hình phụ như *human parsing* (phân đoạn cơ thể người) hoặc chia ảnh thành các dải ngang cố định.
- Ưu: bắt được chi tiết, độ chính xác thường cao hơn global.
- Nhược, và có **ba nhược điểm riêng biệt**, nên nói đủ cả ba:
  - **Nhiễu từ prior:** nếu mô hình phân đoạn cắt sai một vùng, alignment sai theo. Lỗi bị lan truyền.
  - **Chi phí lưu trữ:** mỗi ảnh không còn là một vector mà là *nhiều* vector cục bộ. Gallery phình lên nhiều lần.
  - **Chi phí so sánh:** không còn là một phép tích vô hướng, mà phải ghép cặp nhiều-với-nhiều rồi tổng hợp lại. Điều này phá vỡ giả định của cơ sở dữ liệu vector ở slide 3.

**3. IRRA — hướng thứ ba**
- `Implicit local learning during training` — local token **vẫn tương tác rất mạnh** trong lúc huấn luyện.
- `Global embeddings at inference` — nhưng ở đầu ra thì **không có** nhánh local matching nào cả.
- Nói cách khác: chi tiết được **hấp thụ vào** global embedding thông qua gradient, thay vì được **giữ lại** dưới dạng các vector cục bộ riêng.

### D. Slide này giải quyết vấn đề gì

Slide này **định vị bài báo trong bản đồ nghiên cứu**. Nó trả lời câu hỏi mà bất kỳ người phản biện nào cũng sẽ hỏi: *"cái này khác gì những cái đã có?"*

Nó cũng chuẩn bị nền cho chữ **implicit** — thuật ngữ quan trọng nhất trong tên bài báo — mà bạn sẽ chốt định nghĩa ở slide 7.

### E. Lời thuyết trình

> "Có ba hướng tiếp cận, và nhìn theo trục thời gian thì đây là một sự tiến hóa.
>
> **Hướng đầu tiên là global matching.** Ta nén cả ảnh thành một vector, nén cả câu thành một vector, và đặt loss ở cuối mạng để kéo cặp đúng lại gần nhau. Cách này rất nhanh khi truy hồi. Nhưng vì loss chỉ đặt ở đầu ra, hai luồng ảnh và chữ không trao đổi thông tin ở các tầng giữa, nên các chi tiết nhỏ dễ bị làm nhòe đi.
>
> **Hướng thứ hai là explicit local matching.** Ta tách ảnh thành đầu, thân, chân, hoặc các vùng thuộc tính, rồi ghép với từng cụm từ trong câu. Độ chính xác thường tốt hơn, nhưng phải trả ba loại giá. Thứ nhất, nó cần prior như human parsing, mà nếu phân vùng sai một chỗ thì alignment sai theo. Thứ hai, mỗi ảnh giờ phải lưu nhiều vector cục bộ chứ không còn một vector. Thứ ba, phép so sánh không còn là một tích vô hướng mà là ghép cặp nhiều-nhiều rồi tổng hợp — tức là phá vỡ đúng cái mô hình cơ sở dữ liệu vector mà em vừa trình bày ở slide trước.
>
> **IRRA chọn hướng thứ ba.** Local token vẫn tương tác rất mạnh trong lúc huấn luyện — em nhấn mạnh là *có* tương tác, chứ không phải bỏ. Nhưng ở đầu ra thì không tạo thêm nhánh local matching nào. Kiến thức chi tiết được hấp thụ vào chính global embedding, thay vì được giữ lại thành các vector rời."

### F. Câu chuyển

> "Để có được nền tảng alignment ban đầu tốt, tác giả không ghép hai backbone đơn phương thức mà bắt đầu thẳng từ CLIP. Em xin nói nhanh về CLIP."

---

## Slide 6 — I. Background — Dual-Stream Models and CLIP

**Thời lượng:** ~70 giây

### A. Trên slide có gì

- **Panel trái — `SINGLE-STREAM`:** `[ image tokens + text tokens ]` → mũi tên → `JOINT TRANSFORMER`; đánh giá: *+ Strong cross-modal interaction / − Recomputed for every image–text pair*
- **Panel phải — `DUAL-STREAM • CLIP`:** hai hộp `IMAGE ENCODER` và `TEXT ENCODER` nối bởi một đường ngang, nhãn *joint embedding space*; đánh giá: *+ Precomputed gallery embeddings / + Image–text pre-training / − Limited fine-grained interaction*
- **Thanh đỏ dưới cùng:** `IRRA = full CLIP + interaction only during TRAINING`

### B. Dẫn vào slide

> "Trước khi vào phương pháp, cần một khái niệm nền: mô hình thị giác–ngôn ngữ chia làm hai họ, và lựa chọn họ nào quyết định toàn bộ chi phí hệ thống."

### C. Giải thích từng khái niệm

- **Single-stream** — cho token ảnh và token chữ vào **chung một Transformer** ngay từ đầu. Vì self-attention chạy trên chuỗi hợp nhất nên mọi token ảnh nhìn thấy mọi token chữ và ngược lại → tương tác rất mạnh.
- **Nhược điểm chí mạng của single-stream:** kết quả phụ thuộc vào **cặp**. Muốn biết điểm của ảnh A với câu Q, phải chạy cả mô hình cho cặp (A, Q). Với gallery 20.000 ảnh, một truy vấn cần 20.000 lần chạy Transformer. Không thể tiền tính toán được. → Không dùng được cho cơ sở dữ liệu.
- **Dual-stream** — hai encoder **độc lập** cho hai modality, mỗi bên tự cho ra một vector, chỉ gặp nhau ở phép cosine cuối cùng. Vì độc lập nên có thể **mã hóa gallery trước** (chính là pha offline ở slide 3).
- **CLIP** — *Contrastive Language–Image Pre-training* của OpenAI. Là một mô hình dual-stream được huấn luyện trên lượng rất lớn cặp ảnh–chú thích từ Internet, với mục tiêu đưa ảnh và chú thích đúng của nó lại gần nhau trong không gian chung. Ý nghĩa với bài báo: **CLIP đã có sẵn một không gian nhúng chung tốt** — không phải học từ đầu.
- **Joint embedding space** — nhắc lại từ slide 3, giờ thấy nó đến từ đâu: từ pre-training của CLIP.
- **Nhược điểm của dual-stream:** hai luồng không "nói chuyện" với nhau cho tới tận cuối, nên tương tác chi tiết bị hạn chế. Đây đúng là nhược điểm của *global matching* ở slide 5 — hai slide này khớp vào nhau.
- **Thanh đỏ dưới cùng** là **luận điểm của cả slide**: IRRA lấy toàn bộ CLIP, và bổ sung tương tác **chỉ trong lúc huấn luyện**. Tức là lấy ưu điểm của single-stream mà không phải trả giá của nó khi triển khai.
- **"Full CLIP"** — cần nói rõ: tác giả lập luận rằng một số công trình trước chưa tận dụng trọn vẹn CLIP vì chỉ mượn image encoder, hoặc đóng băng một phần mô hình. IRRA fine-tune **cả hai** encoder.

### D. Slide này giải quyết vấn đề gì

Slide này trả lời: **tại sao lại chọn CLIP làm xương sống?** — và quan trọng hơn, nó cho khán giả công cụ để hiểu vì sao ý tưởng chính của IRRA là hợp lý.

Nếu khán giả nắm được rằng single-stream mạnh-nhưng-đắt còn dual-stream rẻ-nhưng-yếu, thì khi bạn nói "IRRA dùng tương tác kiểu single-stream trong training rồi vứt đi khi test", họ sẽ lập tức thấy đó là một ý tưởng thông minh chứ không phải một thủ thuật tùy tiện.

### E. Lời thuyết trình

> "Các mô hình thị giác–ngôn ngữ thường chia thành hai họ.
>
> **Single-stream** cho token ảnh và token chữ vào chung một Transformer ngay từ đầu. Nhờ vậy tương tác rất mạnh, mô hình hiểu được quan hệ chi tiết giữa từ và vùng ảnh. Nhưng có một vấn đề chí mạng: kết quả phụ thuộc vào cặp. Muốn chấm điểm ảnh A với câu Q, phải chạy cả mô hình cho đúng cặp đó. Với gallery hai mươi nghìn ảnh thì một truy vấn cần hai mươi nghìn lần chạy Transformer — hoàn toàn không dùng được cho cơ sở dữ liệu.
>
> **Dual-stream**, mà CLIP là đại diện, dùng hai encoder độc lập. Mỗi bên tự cho ra một vector, chỉ gặp nhau ở phép cosine cuối cùng. Vì độc lập nên ta mã hóa gallery trước được — đúng pha offline em đã nói. Thêm nữa, CLIP được pre-train trên rất nhiều cặp ảnh và chú thích từ Internet, nên nó đã sẵn có một không gian nhúng chung khá tốt, ta không phải học từ số không.
>
> Nhưng dual-stream có nhược điểm ngược lại: hai luồng không nói chuyện với nhau cho tới tận cuối, nên tương tác chi tiết rất hạn chế.
>
> Và đây là ý tưởng cốt lõi, ở thanh đỏ dưới cùng: **IRRA dùng toàn bộ CLIP, rồi bổ sung tương tác chỉ trong lúc huấn luyện.** Tức là mượn ưu điểm của single-stream trong lúc học, nhưng khi triển khai thì vẫn là dual-stream gọn nhẹ. Tác giả cũng lập luận rằng nhiều công trình trước chưa tận dụng hết CLIP vì chỉ dùng image encoder hoặc đóng băng một phần; IRRA fine-tune cả hai."

### F. Câu chuyển

> "Từ đó, câu hỏi nghiên cứu của bài báo trở nên rất rõ ràng."

### G. Nếu bị hỏi

**"CLIP pre-train trên ảnh Internet, người trong camera giám sát trông rất khác — có hợp không?"**
> Đây là lý do tác giả **fine-tune toàn bộ** CLIP trên dữ liệu person retrieval chứ không đóng băng. Và bằng chứng thực nghiệm ở slide 19 cho thấy CLIP fine-tune trực tiếp đã là một baseline rất mạnh — trên RSTPReid nó còn vượt cả CFine, phương pháp tốt nhất trước đó.

---

# PHẦN PHƯƠNG PHÁP

---

## Slide 7 — II. Proposed Method — Research Question

**Thời lượng:** ~55 giây

### A. Trên slide có gì

- **Hộp lớn trên cùng (câu hỏi nghiên cứu):**
  > *How can fine-grained image–word relations improve global embeddings without part-level supervision or additional retrieval cost?*
- **Ba thẻ đánh số bên dưới:**
  1. `IRR / MLM` — *Implicitly learns fine-grained image–text relations*
  2. `SDM` — *Matches similarity distributions to label distributions*
  3. `FULL CLIP` — *Fine-tunes both image and text encoders*

### B. Dẫn vào slide

> "Ba slide vừa rồi đã dựng đủ bối cảnh. Giờ ta có thể phát biểu chính xác câu hỏi mà bài báo đặt ra."

### C. Giải thích từng khái niệm

**Câu hỏi nghiên cứu — tách làm ba mệnh đề, nên đọc chậm từng mệnh đề:**

| Mệnh đề trong câu hỏi | Nghĩa là gì | Liên hệ slide trước |
|---|---|---|
| *fine-grained image–word relations* | quan hệ giữa **một từ** và **một vùng ảnh**, ví dụ từ "white" ↔ vùng chiếc túi | khó khăn số 3 ở slide 4 |
| *without part-level supervision* | không cần nhãn thủ công kiểu "vùng này là túi", không cần human parsing | nhược điểm của explicit local ở slide 5 |
| *without additional retrieval cost* | khi truy hồi vẫn chỉ một vector ↔ một vector | ràng buộc từ pha online ở slide 3 |

**Chốt định nghĩa chữ "implicit" — đây là chỗ quan trọng nhất của slide:**

Chữ *implicit* **không** có nghĩa là "không dùng local token". Ngược lại, local visual token và local textual token tương tác **rất mạnh** trong lúc train. *Implicit* có đúng hai nghĩa:

1. **Không cần nhãn tường minh** về bộ phận cơ thể hay correspondence từ–vùng. Mô hình tự tìm ra quan hệ đó.
2. **Không có nhánh local matching ở đầu ra.** Quan hệ cục bộ chỉ tồn tại như một *tín hiệu huấn luyện*, không tồn tại như một *thành phần của điểm số truy hồi*.

**Ba đóng góp:**

- **IRR (Implicit Relation Reasoning)** — thực hiện bằng bài toán **MLM** (Masked Language Modeling, mô hình hóa ngôn ngữ có che). Chi tiết ở slide 12–13.
- **SDM (Similarity Distribution Matching)** — một hàm loss mới, khớp phân phối độ tương đồng với phân phối nhãn. Chi tiết ở slide 14.
- **Full CLIP transfer** — fine-tune **cả** image encoder và text encoder, thay vì chỉ mượn một nửa CLIP.

### D. Slide này giải quyết vấn đề gì

Đây là **bản lề của cả bài trình bày**. Từ slide này trở đi ta chuyển từ "mô tả vấn đề" sang "mô tả giải pháp".

Slide này cũng là chỗ bạn **trả trước** một câu hỏi phản biện chắc chắn sẽ có: *"gọi là implicit nhưng vẫn có cross-attention ở local token, sao gọi là implicit được?"*. Nếu định nghĩa rõ ngay ở đây, bạn sẽ không bị vặn ở slide 13.

### E. Lời thuyết trình

> "Câu hỏi trung tâm của bài báo nằm ở hộp trên cùng, và em xin tách nó thành ba vế.
>
> Vế thứ nhất: *làm sao dùng quan hệ chi tiết giữa từ và vùng ảnh* — đây chính là khó khăn số ba ở slide trước, về các chi tiết phân biệt rất nhỏ.
>
> Vế thứ hai: *mà không cần giám sát ở cấp bộ phận* — tức là không cần nhãn thủ công kiểu 'vùng này là cái túi', không cần mô hình human parsing. Đây là để tránh nhược điểm của hướng explicit local.
>
> Vế thứ ba: *và không tăng chi phí truy hồi* — tức là khi test vẫn chỉ so một vector với một vector, giữ nguyên mô hình cơ sở dữ liệu ở slide 3.
>
> Em muốn dừng lại ở chữ **implicit**, vì nó là từ quan trọng nhất trong tên bài báo và cũng dễ bị hiểu sai. Implicit **không** có nghĩa là không dùng local token. Ngược lại, token ảnh và token chữ vẫn tương tác rất mạnh trong lúc huấn luyện. Implicit nghĩa là: một, mô hình không cần nhãn bộ phận nào cả, nó tự tìm ra quan hệ; và hai, không có nhánh đối sánh cục bộ nào ở đầu ra. Quan hệ chi tiết tồn tại như một **tín hiệu học**, chứ không tồn tại như một **thành phần của điểm số truy hồi**.
>
> Ba đóng góp tương ứng là IRR, SDM và chuyển giao toàn bộ CLIP. Em sẽ đi qua từng cái."

### F. Câu chuyển

> "Bây giờ ta ghép ba thành phần này vào một kiến trúc tổng thể."

---

## Slide 8 — II. Proposed Method — IRRA Overview

**Thời lượng:** ~90 giây — **slide quan trọng nhất phần phương pháp, đừng vội**

### A. Trên slide có gì

- **Figure 2** của bài báo chiếm gần trọn slide — sơ đồ kiến trúc đầy đủ
- Ba thẻ đánh số ở dưới: `1 • CLIP DUAL ENCODER`, `2 • SDM + ID`, `3 • IRR / MLM`
- Chú thích: *Dashed modules: removed at inference*

### B. Dẫn vào slide

> "Đây là sơ đồ tổng thể. Em sẽ đi theo đúng ba số ở dưới slide, và xin khán giả để ý một chi tiết: những khối vẽ bằng **nét đứt** sẽ bị bỏ khi triển khai."

### C. Giải thích từng khái niệm

**Hãy chỉ tay theo đúng thứ tự này — đừng nhảy lung tung trên sơ đồ.**

**Khối 1 — CLIP dual encoder (xương sống)**
- Ảnh gốc → Image Encoder (ViT) → một chuỗi visual token, trong đó token `[CLS]` là **global image embedding** $f^v$.
- Câu gốc → Text Encoder → một chuỗi text token, trong đó token `[EOS]` là **global text embedding** $f^t$.
- Đây là phần **duy nhất** còn sống sót khi inference.

**Khối 2 — SDM + ID (giám sát ở cấp toàn cục)**
- Hai vector $f^v, f^t$ đi vào **SDM loss** → căn chỉnh cross-modal.
- Hai vector đó cũng đi vào **ID classifier** → phân loại danh tính.
- Hai loss này tác động **trực tiếp** lên global embedding.

**Khối 3 — IRR / MLM (giám sát ở cấp token)**
- Có **một bản sao thứ hai của câu**, bị che ngẫu nhiên → đi qua **cùng** text encoder (dùng chung tham số) → cho ra masked text token.
- Masked text token làm **Query**; visual token làm **Key** và **Value** → đi vào **Multimodal Interaction Encoder**.
- Kết quả → **MLM head** → dự đoán lại từ bị che.
- Loss này tác động **gián tiếp** lên global embedding, qua đường token.

**Ba điểm cần nhấn mạnh — nếu chỉ nhớ ba điều từ slide này thì là ba điều sau:**

1. **Text encoder được chạy hai lần trong một bước huấn luyện**, với **cùng một bộ tham số**: một lần cho câu gốc (tạo $f^t$), một lần cho câu bị che (tạo token cho MLM). Đây là chi tiết dễ bỏ sót nhất khi nhìn sơ đồ.
2. **Toàn bộ hệ thống được huấn luyện end-to-end**, một lần backward duy nhất.
3. **Các khối nét đứt — interaction encoder, MLM head, ID classifier — đều bị bỏ khi test.** Chỉ còn hai encoder và một phép cosine.

### D. Slide này giải quyết vấn đề gì

Slide này là **tấm bản đồ**. Sáu slide tiếp theo (9–14) mỗi slide phóng to một khối trên sơ đồ này. Nếu khán giả nắm được bản đồ ở đây, họ sẽ không bị lạc ở các slide sau.

Nó cũng là nơi đầu tiên cho thấy **ý tưởng chính thực sự vận hành được**: có tương tác chi tiết (khối 3), nhưng tương tác đó nằm trên một nhánh có thể tháo rời.

### E. Lời thuyết trình

> "Đây là kiến trúc đầy đủ. Em xin đi theo ba số ở dưới slide.
>
> **Số một — CLIP dual encoder.** Ảnh đi qua ViT, câu gốc đi qua text Transformer. Mỗi bên cho ra một chuỗi token, và ta lấy một token đặc biệt làm biểu diễn toàn cục: token CLS cho ảnh, token EOS cho câu. Đây là phần duy nhất còn lại khi triển khai.
>
> **Số hai — SDM và ID loss.** Hai vector toàn cục vừa tạo ra được đưa vào hai hàm loss. SDM lo việc căn chỉnh giữa hai modality. ID loss lo việc gom các mẫu cùng một người lại với nhau. Hai loss này tác động **trực tiếp** lên global embedding.
>
> **Số ba — IRR, hay MLM.** Đây là phần mới của bài báo. Song song với câu gốc, ta tạo một bản sao của câu và che ngẫu nhiên một số từ. Bản sao này đi qua **chính text encoder đó**, dùng chung tham số. Các hidden state thu được sẽ làm query, còn visual token làm key và value, đi vào multimodal interaction encoder. Cuối cùng MLM head phải dự đoán lại từ đã bị che.
>
> Em muốn nhấn ba điều ở slide này.
>
> Thứ nhất, text encoder được chạy **hai lần** trong một bước huấn luyện, với cùng một bộ tham số — nhìn sơ đồ rất dễ bỏ sót chi tiết này.
>
> Thứ hai, toàn bộ hệ thống train end-to-end, chỉ một lần backward.
>
> Thứ ba, và quan trọng nhất về mặt triển khai: các khối vẽ nét đứt — interaction encoder, MLM head và ID classifier — **đều bị bỏ khi test**. Khi đó chỉ còn hai encoder và một phép cosine similarity, đúng như pipeline cơ sở dữ liệu ở slide 3."

### F. Câu chuyển

> "Ta tách kiến trúc này ra, bắt đầu từ cách sinh ra hai vector toàn cục."

---

## Slide 9 — II. Proposed Method — CLIP Dual Encoder

**Thời lượng:** ~65 giây

### A. Trên slide có gì

- **Panel trái — `IMAGE ENCODER • ViT-B/16`:** `384 × 128` → `patch 16 × 16` → `24 × 8 = 192 visual tokens` → `[CLS] → f_v`, chú thích `12 Transformer blocks`
- **Panel phải — `TEXT ENCODER • Transformer`:** `BPE vocabulary` `49,152` → `[SOS] token₁ … token₇₇ [EOS]` → `[EOS] → f_t`, chú thích `12 Transformer blocks`

### B. Dẫn vào slide

> "Ta phóng to khối số một. Câu hỏi ở đây rất cụ thể: một tấm ảnh và một câu chữ biến thành vector bằng cách nào?"

### C. Giải thích từng khái niệm

**Phía ảnh:**

- **ViT-B/16** — Vision Transformer, phiên bản Base, patch size 16. "Base" nghĩa là 12 block, chiều ẩn 768, 12 head.
- **`384 × 128`** — kích thước ảnh đầu vào. Lưu ý tỷ lệ **3:1 theo chiều dọc**, không phải ảnh vuông — vì ảnh người đứng thì cao hơn rộng. Đây là lựa chọn riêng cho bài toán person retrieval.
- **Patch `16 × 16`** — ảnh bị cắt thành lưới ô vuông 16×16 pixel. Mỗi ô được làm phẳng và chiếu tuyến tính thành một vector 768 chiều. Từ đây trở đi, Transformer không còn "thấy" pixel nữa, chỉ thấy một chuỗi token.
- **`24 × 8 = 192 visual tokens`** — phép tính: $384/16 = 24$ hàng, $128/16 = 8$ cột → 192 patch. Cộng thêm token `[CLS]` là **193 token**.
- **`[CLS]`** — một token đặc biệt được **thêm vào** đầu chuỗi, không tương ứng với vùng ảnh nào cả. Vì self-attention cho phép nó nhìn mọi patch, nó dần trở thành nơi **tổng hợp thông tin toàn ảnh**. Sau khi chiếu, nó chính là $f^v$.

**Phía chữ:**

- **BPE (Byte Pair Encoding)** — cách tách văn bản thành token. Nó **không** tách theo từ mà theo các mảnh từ xuất hiện nhiều. Ưu điểm: không bao giờ gặp từ lạ hoàn toàn, vì từ hiếm sẽ được tách thành nhiều mảnh nhỏ.
- **Vocabulary `49,152`** — kích thước từ điển. ⚠️ *Xem mục "Điểm cần sửa trên deck" ở cuối file: con số trong code là **49,408**.*
- **`[SOS]` / `[EOS]`** — token đánh dấu bắt đầu và kết thúc câu. Câu thật nằm giữa hai token này, tối đa **77 token** kể cả hai token đặc biệt.
- **`[EOS] → f_t`** — hidden state tại vị trí `[EOS]` được lấy làm vector câu. Lý do sẽ giải thích ở slide 11 (liên quan causal mask) — ở đây chỉ cần nói: vì `[EOS]` đứng cuối nên nó đã "nhìn" qua toàn bộ câu.
- **Cùng không gian** — cả hai vector đều được chiếu về **512 chiều**, đúng không gian nhúng chung của CLIP.

**Một câu cần nói và rất dễ quên:**
> Các local token — 192 visual token và các text token — **không** trực tiếp tham gia tính điểm khi test. Nhưng chúng **được giữ lại** để huấn luyện IRR. Đây chính là cầu nối sang slide 12.

### D. Slide này giải quyết vấn đề gì

Slide này **cụ thể hóa** khái niệm trừu tượng "embedding" ở slide 3 thành những con số thật. Sau slide này, khi bạn nói "visual token", khán giả biết chính xác đó là 192 vector, mỗi vector ứng với một ô 16×16 pixel trên ảnh.

Đó là điều kiện cần để hiểu slide 13 (cross-attention): phải biết Key và Value là **cái gì** trước khi nói chúng được dùng ra sao.

### E. Lời thuyết trình

> "Bên ảnh, mô hình dùng CLIP ViT-B/16. Ảnh được resize về 384 nhân 128 — để ý là tỷ lệ dọc ba trên một, vì ảnh người đứng thì cao hơn rộng. Ảnh được cắt thành các ô 16 nhân 16 pixel: 384 chia 16 được 24, 128 chia 16 được 8, nên ta có 192 patch. Mỗi patch được chiếu thành một vector, và thêm một token đặc biệt là CLS. Token CLS không ứng với vùng ảnh nào cả, nhưng vì self-attention cho phép nó nhìn mọi patch, sau 12 block nó trở thành nơi tổng hợp thông tin toàn ảnh. Sau phép chiếu, nó chính là vector ảnh toàn cục f-v.
>
> Bên chữ, văn bản được đưa về chữ thường và tokenize bằng BPE. BPE tách theo mảnh từ chứ không theo từ nguyên vẹn, nên không bao giờ gặp trường hợp từ hoàn toàn lạ. Chuỗi token được kẹp giữa SOS và EOS, tối đa 77 token. Hidden state tại vị trí EOS được lấy làm vector câu — em sẽ giải thích lý do ở slide sau, khi nói về causal mask.
>
> Cả hai vector đều được chiếu về 512 chiều, cùng một không gian nhúng.
>
> Có một điểm em muốn lưu ý vì nó dẫn thẳng sang phần sau: các local token — 192 visual token và các text token — không trực tiếp tham gia tính điểm khi test. Nhưng chúng **được giữ lại** để huấn luyện IRR. Đó chính là nguyên liệu của phần tiếp theo."

### F. Câu chuyển

> "Hai slide tiếp theo em xin đi sâu vào bên trong mỗi encoder, vì hiểu được cấu trúc block thì mới hiểu được gradient của IRR đi vào đâu."

---

## Slide 10 — II. Proposed Method — Inside the ViT Image Encoder

**Thời lượng:** ~80 giây

### A. Trên slide có gì

- **Hình lớn bên trái:** sơ đồ chi tiết luồng dữ liệu trong ViT
- **Cột phải — thẻ `ViT-B/16 • 12 BLOCKS`**, năm bước:
  1. Patch embedding + position
  2. Pre-LN multi-head self-attention
  3. Residual connection
  4. Pre-LN MLP: 768 → 3072 → 768
  5. `[CLS]` collects global visual context
- **Hộp công thức dưới cùng:**
  `x ← x + MSA(LN(x))` / `x ← x + MLP(LN(x))`

### B. Dẫn vào slide

> "Slide trước nói ảnh biến thành 192 token. Slide này nói 192 token đó được xử lý thế nào — và quan trọng hơn, vì sao chúng giữ được thông tin cục bộ."

### C. Giải thích từng khái niệm

- **Positional embedding** — bản thân self-attention không biết thứ tự hay vị trí. Nếu không cộng thêm thông tin vị trí, mô hình sẽ không phân biệt được patch ở vùng đầu với patch ở vùng chân. Đây là một vector học được, cộng vào từng token.
- **Pre-LayerNorm (Pre-LN)** — LayerNorm được đặt **trước** khối attention/MLP chứ không phải sau. Đây là biến thể chuẩn của CLIP, giúp huấn luyện mạng sâu ổn định hơn.
- **MSA — Multi-head Self-Attention.** Ý nghĩa cần nói bằng lời, không nói bằng công thức:
  > Mỗi token nhìn vào **tất cả** các token khác, tự quyết định token nào đáng chú ý, rồi tổng hợp thông tin từ chúng theo trọng số.

  Cụ thể ở đây: một patch ở vùng áo có thể nhìn sang patch ở vùng túi, vùng quần, vùng giày. Và `[CLS]` có thể nhìn tất cả. **"Multi-head"** nghĩa là làm việc đó song song 12 lần với 12 phép chiếu khác nhau, để mỗi "đầu" chú ý một loại quan hệ khác nhau.
- **Residual connection** — `x + f(x)` thay vì `f(x)`. Hai tác dụng: giữ cho thông tin gốc không bị mất qua từng lớp, và tạo một "đường cao tốc" cho gradient chảy ngược về các lớp đầu. **Đây là lý do kỹ thuật khiến gradient của MLM ở slide 12 có thể đi ngược tận vào patch embedding.**
- **MLP `768 → 3072 → 768`** — hai lớp tuyến tính, mở rộng chiều lên gấp bốn rồi nén lại, với activation **QuickGELU** ở giữa. Nếu attention là nơi các token *trao đổi* thông tin, thì MLP là nơi mỗi token *xử lý riêng* thông tin của mình.
- **`[CLS]` collects global visual context** — sau 12 vòng lặp như vậy, CLS đã tích lũy thông tin từ mọi vùng ảnh.
- **Đầu ra cuối cùng:** LayerNorm → chiếu tuyến tính 768 → 512. Token đầu tiên thành $f^v$; **192 token còn lại được giữ nguyên** làm Key/Value cho IRR.

### D. Slide này giải quyết vấn đề gì

Slide này trả lời hai câu hỏi ngầm:

1. **"Visual token có thực sự chứa thông tin cục bộ không?"** — Có. Mỗi token bắt nguồn từ một ô 16×16 pixel cụ thể và giữ liên hệ với vị trí đó nhờ positional embedding. Đây là điều kiện cần để cross-attention ở slide 13 có ý nghĩa: text token mới "hỏi đúng vùng" được.
2. **"Gradient của MLM có đi được tới đây không?"** — Có, nhờ residual connection và nhờ việc IRRA **không đóng băng** CLIP. Đây là mắt xích để kết luận ở slide 16 rằng "bỏ interaction module khi test không làm mất kiến thức".

### E. Lời thuyết trình

> "Bên trong image encoder, ảnh trước hết được chia thành patch 16 nhân 16 và chiếu thành token 768 chiều. Ta thêm token CLS và cộng positional embedding — bước này cần thiết vì bản thân self-attention không biết vị trí, nếu không cộng thì mô hình không phân biệt được patch ở vùng đầu với patch ở vùng chân.
>
> Mỗi block của CLIP ViT dùng kiến trúc pre-LayerNorm, tức chuẩn hóa trước rồi mới attention. Multi-head self-attention cho phép mỗi token nhìn vào tất cả token khác và tự quyết định token nào đáng chú ý. Cụ thể, một patch ở vùng áo có thể nhìn sang patch ở vùng túi hay vùng giày, và CLS thì nhìn được tất cả. Multi-head nghĩa là làm việc đó song song mười hai lần với mười hai phép chiếu khác nhau, để mỗi đầu bắt một loại quan hệ.
>
> Kết quả attention được cộng ngược với đầu vào qua residual connection. Residual có hai tác dụng: giữ thông tin gốc không bị mất, và tạo đường cho gradient chảy ngược về các lớp đầu — điều này sẽ quan trọng ở phần sau. Nửa sau của block là MLP mở rộng chiều lên bốn lần rồi nén lại, qua QuickGELU. Nếu attention là nơi các token trao đổi thông tin thì MLP là nơi mỗi token tự xử lý thông tin của mình.
>
> Sau mười hai block như vậy, toàn bộ token đi qua LayerNorm và một phép chiếu vào không gian nhúng chung. Token đầu tiên trở thành f-v toàn cục. Nhưng em nhấn mạnh: **192 token còn lại không bị vứt đi** — chúng chính là Key và Value cho phần IRR.
>
> Và một điểm then chốt: IRRA **không đóng băng** nhánh này. Gradient từ SDM, từ ID và từ MLM đều có thể cập nhật ViT."

### F. Câu chuyển

> "Text encoder dùng cùng loại block, nhưng cơ chế attention có một khác biệt quan trọng: causal mask."

---

## Slide 11 — II. Proposed Method — Inside the CLIP Text Encoder

**Thời lượng:** ~75 giây

### A. Trên slide có gì

- **Hình lớn bên trái:** sơ đồ luồng dữ liệu trong text Transformer
- **Cột phải — thẻ `TEXT • 12 BLOCKS`**, năm bước:
  1. BPE token + position
  2. **Causal self-attention**
  3. Same Pre-LN residual block
  4. `[EOS]` summarizes the prefix
  5. Linear projection → `f_t`
- **Hộp nhấn mạnh:** *token i attends only to positions ≤ i*

### B. Dẫn vào slide

> "Cấu trúc block gần như y hệt slide trước, nên em chỉ nói vào đúng một điểm khác biệt — nhưng điểm khác biệt đó lại giải thích một câu hỏi từ slide 9."

### C. Giải thích từng khái niệm

- **Causal self-attention (attention nhân quả / attention có mặt nạ tam giác)** — token ở vị trí $i$ **chỉ được nhìn** các vị trí từ $1$ đến $i$, không nhìn được về phía sau. Cơ chế: một mặt nạ tam giác đặt lên ma trận attention, che toàn bộ phần tương lai.
- **Vì sao CLIP làm vậy?** — Text encoder của CLIP kế thừa thiết kế mô hình ngôn ngữ tự hồi quy (kiểu GPT). IRRA giữ nguyên để tận dụng trọng số pre-train.
- **Hệ quả rất cụ thể, và đây là câu trả lời cho slide 9:**
  > Vì mỗi token chỉ thấy phần đứng trước nó, và `[EOS]` là token **cuối cùng**, nên `[EOS]` là token **duy nhất đã nhìn thấy toàn bộ câu**. Đó chính là lý do ta lấy hidden state tại `[EOS]` làm vector câu — chứ không phải lấy trung bình các token hay lấy token đầu.
- **`[EOS] summarizes the prefix`** — "prefix" ở đây là toàn bộ nội dung câu đứng trước nó.
- **Phần còn lại của block** — giống hệt ViT: `LN → attention → residual → LN → MLP → residual`. Không cần giải thích lại.
- **Linear projection → $f^t$** — chiếu về 512 chiều, cùng không gian với $f^v$.

**Điểm phải nói, và là mắt xích logic của cả phần phương pháp:**

Trong **một** bước huấn luyện IRRA, text encoder được chạy **hai lượt** với **cùng một bộ tham số**:

| Lượt | Đầu vào | Đầu ra dùng để | 
|---|---|---|
| 1 | câu **gốc** | lấy `[EOS]` → $f^t$ → cho SDM và ID loss |
| 2 | câu **bị che** | lấy toàn bộ token → làm Query cho interaction encoder → cho MLM |

Khi backward, gradient của **cả hai lượt được cộng vào cùng một bộ tham số**. Đây chính là cơ chế khiến việc học MLM cải thiện được vector $f^t$ dùng khi truy hồi.

### D. Slide này giải quyết vấn đề gì

Ba việc:

1. **Trả một món nợ từ slide 9** — giải thích vì sao lấy `[EOS]` chứ không phải token khác.
2. **Chuẩn bị cho slide 12** — muốn hiểu MLM thì phải biết text encoder chạy hai lượt.
3. **Gieo mầm cho kết luận ở slide 16** — chia sẻ tham số chính là lý do "tháo nhánh phụ đi mà không mất kiến thức".

### E. Lời thuyết trình

> "Text encoder có cùng cấu trúc residual pre-LN như ViT, nên em không lặp lại. Khác biệt duy nhất nằm ở self-attention: nó dùng **causal mask**. Token ở vị trí i chỉ nhìn được các vị trí từ đầu câu đến i, không nhìn được về phía sau. Đây là thiết kế mà CLIP kế thừa từ mô hình ngôn ngữ tự hồi quy, và IRRA giữ nguyên để dùng được trọng số pre-train.
>
> Hệ quả của nó chính là câu trả lời cho thắc mắc ở slide trước. Vì mỗi token chỉ thấy phần đứng trước, mà EOS là token cuối cùng, nên **EOS là token duy nhất đã nhìn thấy toàn bộ câu**. Đó là lý do ta lấy hidden state tại EOS làm vector câu, chứ không lấy trung bình hay lấy token đầu. Sau LayerNorm và text projection, nó trở thành f-t.
>
> Và đây là điểm em cho là quan trọng nhất slide này. Trong **một** bước huấn luyện IRRA, text encoder được chạy **hai lượt**, dùng **chung một bộ tham số**. Lượt thứ nhất nhận câu gốc, để tạo f-t cho SDM và ID loss. Lượt thứ hai nhận câu bị che, để tạo các token hidden state cho nhánh MLM.
>
> Khi backward, gradient của cả hai lượt được **cộng vào cùng một bộ tham số text encoder**. Chính cơ chế chia sẻ tham số này là lý do vì sao việc học điền từ bị che lại cải thiện được vector dùng khi truy hồi. Em sẽ quay lại ý này ở slide Train và Inference."

### F. Câu chuyển

> "Đã biết hai encoder sinh ra token thế nào, giờ ta xem IRRA dùng các token đó để tạo tín hiệu học cục bộ ra sao."

---

## Slide 12 — II. Proposed Method — IRR through MLM

**Thời lượng:** ~85 giây — **đây là ý tưởng cốt lõi của bài báo**

### A. Trên slide có gì

- **Cột trái:**
  - `ORIGINAL TEXT`: *… gray shoes and a white purse around her waist.*
  - `MASKED TEXT`: *… gray [MASK] and a [MASK] purse [MASK] her waist.*
  - `Predictions: shoes • white • around`
  - Hộp quy tắc: *Select 15% of tokens* / *80% [MASK] • 10% random • 10% unchanged*
- **Cột phải:** **Figure 3** của bài báo — minh họa từ `bag` làm mỏ neo, các embedding ảnh và chữ hội tụ về nó

### B. Dẫn vào slide

> "Đây là ý tưởng trung tâm của bài báo, và em nghĩ nó rất đẹp: tác giả không phát minh ra một cơ chế alignment mới, mà mượn một bài toán quen thuộc từ NLP rồi đặt nó vào bối cảnh đa phương thức."

### C. Giải thích từng khái niệm

- **MLM — Masked Language Modeling.** Bài toán vốn dùng để pre-train BERT: che ngẫu nhiên một số từ trong câu, bắt mô hình đoán lại từ đã bị che.
- **Điểm khác biệt mấu chốt so với BERT:** ở BERT, mô hình chỉ có **ngữ cảnh chữ** để đoán. Ở IRRA, mô hình có **ngữ cảnh chữ cộng thêm tấm ảnh**.

  → Và đây chính là toàn bộ mẹo của bài báo. Hãy giải thích bằng ví dụ trên slide:

  > Che từ `white` trong cụm `a [MASK] purse`. Nếu chỉ nhìn phần câu còn lại, có hàng chục màu đều hợp ngữ pháp: black, red, brown, blue… Mô hình **không thể** đoán đúng nếu chỉ dựa vào chữ.
  >
  > Để đoán đúng `white`, mô hình **buộc phải** tìm cho ra vùng ảnh chứa chiếc túi, và đọc màu của nó.

  Nói cách khác: **bài toán MLM ép mô hình phải học quan hệ từ ↔ vùng ảnh, mà không cần ai gán nhãn vùng nào là cái túi cả.** Đó chính xác là nghĩa của chữ *implicit* ở slide 7.

- **Ba từ bị che trong ví dụ thể hiện ba loại quan hệ khác nhau** — nên chỉ ra để cho thấy MLM học nhiều thứ:
  - `shoes` — **danh từ, tên vật thể** → cần nhận diện đối tượng trong ảnh
  - `white` — **tính từ, thuộc tính** → cần đọc màu ở đúng vùng
  - `around` — **giới từ, quan hệ không gian** → cần hiểu bố cục ("quanh eo")
- **Quy tắc 15% và 80/10/10** — kế thừa nguyên từ BERT:
  - Chọn ngẫu nhiên **15%** token để làm nhiệm vụ dự đoán.
  - Trong 15% đó: **80%** thay bằng `[MASK]`, **10%** thay bằng một token ngẫu nhiên, **10%** giữ nguyên.
  - **Vì sao phải làm phức tạp vậy?** Nếu luôn thay bằng `[MASK]`, mô hình sẽ chỉ học cách xử lý token `[MASK]` — mà khi test thì không có `[MASK]` nào cả, gây lệch giữa train và test. Trộn thêm token ngẫu nhiên và token giữ nguyên buộc mô hình phải "đề phòng" ở **mọi** vị trí.
  - *(Trong code: nếu không có token nào được chọn thì ép mask ít nhất một token.)*
- **Hàm loss** — cross-entropy chỉ tính trên các vị trí bị chọn:

  $$\mathcal L_{\mathrm{IRR}} = -\frac{1}{|\mathcal M|}\sum_{i\in\mathcal M}\log p_\theta\!\left(w_i \mid \hat T, I\right)$$

  Trong đó $\mathcal M$ là tập vị trí bị che, $\hat T$ là câu bị che, $I$ là ảnh. Code dùng `CrossEntropyLoss(ignore_index=0)` — các vị trí không được chọn có nhãn 0 và bị bỏ qua hoàn toàn.
- **Figure 3 bên phải — cách giải thích:** từ thật (`bag`) có một embedding **tĩnh**, cố định trong từ điển. Nó đóng vai trò **mỏ neo**. Mô hình phải kéo cả biểu diễn của vùng ảnh lẫn biểu diễn của ngữ cảnh câu về phía mỏ neo đó. Vì cả hai cùng bị kéo về một điểm, chúng **gián tiếp** được kéo lại gần nhau. Đó là cơ chế alignment.

### D. Slide này giải quyết vấn đề gì

Slide này giải quyết **khó khăn số 3 ở slide 4** (chi tiết phân biệt rất nhỏ) mà **không vi phạm ràng buộc ở slide 7** (không cần nhãn bộ phận).

Nó cũng là câu trả lời cho câu hỏi hiển nhiên *"làm sao bắt mô hình chú ý đến chi tiết mà không nói cho nó biết chi tiết nằm ở đâu?"* — câu trả lời: **đặt cho nó một bài toán mà nó không thể giải nếu không nhìn vào chi tiết.**

### E. Lời thuyết trình

> "Đây là ý tưởng cốt lõi của bài báo. Tác giả mượn bài toán Masked Language Modeling từ BERT: che ngẫu nhiên một số từ trong câu và bắt mô hình đoán lại.
>
> Nhưng có một khác biệt quyết định. Ở BERT, mô hình chỉ có ngữ cảnh chữ để đoán. Ở đây, mô hình có ngữ cảnh chữ **cộng thêm tấm ảnh**.
>
> Em xin lấy đúng ví dụ trên slide. Ta che từ *white* trong cụm *a mask purse*. Nếu chỉ nhìn phần câu còn lại, có hàng chục màu đều hợp ngữ pháp: đen, đỏ, nâu, xanh. Mô hình **không có cách nào** đoán đúng nếu chỉ dựa vào chữ. Để đoán đúng là *white*, nó **buộc phải** tìm ra vùng ảnh chứa chiếc túi và đọc màu của nó.
>
> Và đây chính là mẹo: bài toán MLM **ép** mô hình học quan hệ giữa từ và vùng ảnh, mà không cần bất kỳ ai gán nhãn 'vùng này là cái túi'. Đó đúng là nghĩa của chữ *implicit* mà em đã định nghĩa ở slide bảy.
>
> Ba từ bị che trong ví dụ cũng thể hiện ba loại quan hệ khác nhau: *shoes* là danh từ, cần nhận diện vật thể; *white* là tính từ, cần đọc thuộc tính màu ở đúng vùng; còn *around* là giới từ, cần hiểu quan hệ không gian.
>
> Về quy tắc che: ta chọn 15% token, trong đó 80% thay bằng MASK, 10% thay bằng token ngẫu nhiên, 10% giữ nguyên. Đây là quy tắc của BERT. Lý do phải trộn như vậy là vì nếu luôn thay bằng MASK thì mô hình chỉ học cách xử lý token MASK, mà khi test thì không có MASK nào cả — sẽ lệch giữa train và test.
>
> Hình bên phải là cách tác giả giải thích cơ chế. Từ thật, ví dụ *bag*, có một embedding tĩnh cố định trong từ điển, đóng vai trò mỏ neo. Mô hình phải kéo cả biểu diễn của vùng ảnh lẫn biểu diễn của ngữ cảnh câu về phía mỏ neo đó. Vì cả hai cùng bị kéo về một điểm, chúng gián tiếp được kéo lại gần nhau. Đó là cách alignment xảy ra."

### F. Câu chuyển

> "Để dự đoán được từ bị che bằng cả hai modality, IRRA cần một module cho phép chữ 'hỏi' ảnh. Đó là nội dung slide tiếp theo."

### G. Nếu bị hỏi

**"Vì sao không dùng Masked Image Modeling, che vùng ảnh thay vì che từ?"**
> Bài báo không thử hướng đó. Về mặt trực giác, che từ dễ tạo tín hiệu sắc nét hơn vì mục tiêu dự đoán là một token rời rạc trong từ điển hữu hạn, trong khi dự đoán lại pixel là bài toán hồi quy khó định nghĩa hơn. Đây là một hướng mở rộng hợp lý.

---

## Slide 13 — II. Proposed Method — Multimodal Interaction

**Thời lượng:** ~80 giây

### A. Trên slide có gì

- **Hình trên:** **Figure 4** của bài báo — ba kiểu module tương tác đặt cạnh nhau
- **Thẻ trái dưới:** `Q` → *masked text tokens*; `K, V` → *visual tokens*
- **Thẻ phải dưới:** *One-way cross-attention → 4 Transformer blocks* / *hidden size = 512 • 8 heads*

### B. Dẫn vào slide

> "Slide trước đặt ra yêu cầu: token chữ phải lấy được thông tin từ ảnh. Slide này là cơ chế thực hiện yêu cầu đó."

### C. Giải thích từng khái niệm

**Q, K, V — nên giải thích bằng ẩn dụ tra cứu, đừng giải thích bằng công thức:**

| Ký hiệu | Tên | Vai trò | Ở đây là gì |
|---|---|---|---|
| **Q** | Query | "tôi đang cần tìm gì" | hidden state của các token trong **câu bị che** |
| **K** | Key | "tôi chứa nội dung gì" | **visual token** (192 vùng ảnh) |
| **V** | Value | "nội dung thực sự lấy về" | **visual token** |

Cơ chế: mỗi Query so khớp với toàn bộ Key để tính trọng số chú ý, rồi lấy tổng có trọng số của các Value.

$$\operatorname{MCA}(Q,K,V)=\operatorname{softmax}\!\left(\frac{QK^\top}{\sqrt d}\right)V$$

**Diễn giải một câu — nên nói đúng câu này:**
> Token chữ chủ động **hỏi** ảnh: *"vùng nào của bức ảnh liên quan đến tôi?"*, rồi mang thông tin từ vùng đó về.

- **Cross-attention vs self-attention** — self-attention thì Q, K, V cùng đến từ một nguồn. Cross-attention thì Q đến từ nguồn này, K/V đến từ nguồn khác. Đây là cách chuẩn để một modality lấy thông tin từ modality khác.
- **One-way (một chiều)** — chỉ có chữ hỏi ảnh, **không** có chiều ngược lại. Lý do rất thực dụng: nhiệm vụ cuối cùng là **dự đoán token văn bản**, nên chỉ cần làm giàu biểu diễn phía văn bản. Làm thêm chiều ngược lại là dư thừa với mục tiêu này.
- **`4 Transformer blocks`** — sau cross-attention, kết quả đi tiếp qua 4 block self-attention + feed-forward thông thường, để các token văn bản (đã có thêm thông tin ảnh) tiếp tục trao đổi với nhau.
- **`hidden size = 512`, `8 heads`** — khớp với chiều của không gian nhúng CLIP; 512 ÷ 64 = 8 head. *(Trong code: `nn.MultiheadAttention(512, 512//64)` và `Transformer(width=512, layers=4, heads=8)`, tham số `cmt_depth` mặc định bằng 4.)*
- **MLM head** — sau cùng: `Linear → QuickGELU → LayerNorm → Linear(vocab_size)`, cho ra phân phối trên toàn bộ từ điển tại mỗi vị trí bị che.

**Ba kiểu module trong Figure 4 — nói ngắn, đây là phần so sánh thiết kế:**

| Kiểu | Cách làm | Vì sao IRRA không chọn |
|---|---|---|
| **(a) Co-attention** | hai nhánh Transformer song song, hai modality hỏi nhau qua lại | nhiều tham số nhất (33.62M), chậm nhất (24.30 ms) |
| **(b) Merged attention** | nối toàn bộ token hai modality thành một chuỗi dài rồi self-attend | chuỗi dài → chi phí attention tăng theo bình phương |
| **(c) Ours — one-way** | chỉ chữ hỏi ảnh | đúng nhu cầu của MLM, rẻ nhất (6.42 ms) |

### D. Slide này giải quyết vấn đề gì

Slide này là **phần kỹ thuật hiện thực hóa ý tưởng ở slide 12**. Slide 12 nói *cần gì*, slide 13 nói *làm bằng cách nào*.

Nó cũng cho thấy tác giả **có cân nhắc thiết kế**, không chọn bừa: có ba phương án, và phương án được chọn vừa rẻ nhất vừa khớp nhất với nhiệm vụ. Đây là chỗ để nhấn rằng bài báo chú ý đến chi phí — phù hợp với chủ đề học phần.

### E. Lời thuyết trình

> "Cơ chế ở đây là cross-attention, và em xin giải thích bằng ẩn dụ tra cứu.
>
> Trong attention có ba thành phần: Query là *tôi đang cần tìm gì*, Key là *tôi chứa nội dung gì*, và Value là *nội dung thực sự được lấy về*. Mỗi Query so khớp với toàn bộ Key để tính trọng số, rồi lấy tổng có trọng số của các Value.
>
> Ở IRRA, **Query đến từ câu bị che, còn Key và Value đến từ visual token**. Nói bằng lời: token chữ chủ động hỏi ảnh — *vùng nào của bức ảnh liên quan đến tôi?* — rồi mang thông tin từ vùng đó về. Đây chính xác là thứ mà bài toán điền từ ở slide trước cần.
>
> Thiết kế này là **một chiều**: chỉ có chữ hỏi ảnh, không có chiều ngược lại. Lý do rất thực dụng — nhiệm vụ cuối cùng là dự đoán token văn bản, nên chỉ cần làm giàu phía văn bản là đủ.
>
> Sau cross-attention, kết quả đi qua bốn Transformer block nữa để các token văn bản, giờ đã mang thông tin ảnh, tiếp tục trao đổi với nhau. Kích thước ẩn là 512, tám head, khớp với chiều không gian nhúng của CLIP.
>
> Hình trên slide so sánh ba lựa chọn thiết kế. **Co-attention** duy trì hai nhánh Transformer song song cho hai modality hỏi nhau qua lại — mạnh nhưng nhiều tham số nhất và chậm nhất. **Merged attention** nối toàn bộ token của hai modality thành một chuỗi dài rồi self-attend — chi phí attention tăng theo bình phương độ dài chuỗi. IRRA chọn phương án một chiều: đúng nhu cầu của MLM, và như em sẽ trình bày ở phần kết quả, nhanh hơn khoảng ba lần."

### F. Câu chuyển

> "IRR lo phần tương tác ở cấp token. Còn ở cấp vector toàn cục, IRRA thay hàm loss ghép cặp thông thường bằng SDM."

---

## Slide 14 — II. Proposed Method — Similarity Distribution Matching

**Thời lượng:** ~85 giây

### A. Trên slide có gì

- **Thẻ `SDM • BIDIRECTIONAL`** với ba công thức:
  - `p(i,j) = exp(sim(i,j)/τ) / Σₖ exp(sim(i,k)/τ)`
  - `q(i,j) = y(i,j) / Σₖ y(i,k)`
  - `LSDM = KL(p i→t ‖ q i→t) + KL(p t→i ‖ q t→i)`
- **Hộp:** `τ = 0.02` → *sharper distribution → emphasizes hard negatives*
- **Cột phải:** hai lưới 5×5 xếp chồng — `p • similarity distribution` ở trên, `q • label distribution` ở dưới, nối bởi mũi tên `KL`; một ô được chú thích `hard negative`

### B. Dẫn vào slide

> "Từ đây ta rời cấp token và quay về cấp vector toàn cục. Câu hỏi là: có hai vector rồi, ta dạy chúng nằm đúng chỗ bằng cách nào?"

### C. Giải thích từng khái niệm

**Bối cảnh: mini-batch và ma trận tương đồng**

- Trong một **mini-batch** có $N$ cặp (ảnh, câu). Ta tính cosine similarity giữa **mọi** ảnh với **mọi** câu → một **ma trận $N \times N$**. Đây chính là hai lưới bên phải slide.
- Mỗi **hàng** của ma trận = một ảnh được so với tất cả các câu trong batch.

**$p$ — phân phối dự đoán**

- Lấy một hàng của ma trận similarity, cho qua **softmax** → được một phân phối xác suất. Ý nghĩa: *"theo mô hình hiện tại, ảnh $i$ tin rằng câu nào là của nó, với xác suất bao nhiêu"*.
- **$\tau$ — temperature (nhiệt độ).** Chia similarity cho $\tau$ trước khi softmax.
  - $\tau$ nhỏ → phân phối **nhọn**, chênh lệch nhỏ giữa các similarity bị khuếch đại thành chênh lệch lớn về xác suất.
  - $\tau$ lớn → phân phối **phẳng**, mọi thứ gần như đều nhau.
  - Ở đây $\tau = 0.02$, tức nhân similarity với 50 — rất nhọn. **Hệ quả:** một negative có similarity cao sẽ nhận xác suất lớn, tạo gradient mạnh → mô hình bị ép phải xử lý nó. Đó là ý nghĩa của dòng *emphasizes hard negatives*.
- **Hard negative (mẫu âm khó)** — một cặp ảnh–câu **không** đúng nhưng mô hình lại chấm điểm cao. Ví dụ: hai người khác nhau cùng mặc áo trắng quần đen. Đây đúng là trường hợp gây lỗi ở slide 4, nên xử lý được hard negative là xử lý đúng chỗ đau.

**$q$ — phân phối nhãn**

- $y_{i,j} = 1$ nếu ảnh $i$ và câu $j$ **cùng một danh tính**, ngược lại bằng 0.
- Chuẩn hóa để tổng bằng 1: nếu có $m$ câu cùng danh tính với ảnh $i$ thì mỗi câu nhận xác suất $1/m$.
- **Điểm tinh tế cần nói:** nhãn dựa trên **danh tính**, không phải trên chỉ số cặp. Nên nếu trong batch có nhiều ảnh/câu của cùng một người, SDM coi **tất cả** đều là positive. Đây là khác biệt so với InfoNCE của CLIP, vốn chỉ coi đường chéo là đúng.

**KL divergence**

- Đo độ lệch giữa hai phân phối. Bằng 0 khi trùng khớp hoàn toàn.
- Mục tiêu: kéo $p$ (mô hình đang nghĩ) về $q$ (sự thật).

**Bidirectional (hai chiều)**

- $p^{i\to t}$ — chuẩn hóa theo **hàng**: mỗi ảnh so với mọi câu.
- $p^{t\to i}$ — chuẩn hóa theo **cột**: mỗi câu so với mọi ảnh.
- Cộng cả hai → tối ưu cả hai chiều truy hồi. Cần thiết vì bài toán thực tế là text→image, nhưng ràng buộc cả hai chiều cho không gian nhúng chặt chẽ hơn.

**Ý nghĩa cốt lõi — câu cần chốt:**
> Các loss ghép cặp thông thường chỉ quan tâm **"cặp đúng có điểm cao không"**. SDM quan tâm **"toàn bộ hình dạng phân phối có đúng không"** — tức là vừa đẩy positive lên, vừa chủ động dìm các negative đang nổi lên.

*(Đối chiếu code `model/objectives.py::compute_sdm`: `logit_scale = 1/temperature = 50`; `labels_distribute = labels / labels.sum(dim=1)`; KL được tính theo chiều $\mathrm{KL}(p\Vert q)$ với `epsilon = 1e-8` để tránh log của 0.)*

### D. Slide này giải quyết vấn đề gì

SDM giải quyết **khó khăn số 1 và số 3 ở slide 4** ở cấp toàn cục:

- Nhiều ảnh cùng một người → nhờ nhãn theo danh tính, tất cả đều được coi là positive, nên mô hình không bị phạt oan khi kéo chúng lại gần nhau.
- Nhiều người trông giống nhau (hard negative) → nhờ $\tau$ nhỏ, các trường hợp này bị khuếch đại và bị xử lý mạnh.

Nếu IRR dạy mô hình *nhìn vào đâu*, thì SDM dạy mô hình *xếp mọi thứ vào đúng chỗ so với nhau*. Hai việc khác nhau, bổ sung cho nhau — và ablation ở slide 20 sẽ chứng minh đúng điều này.

### E. Lời thuyết trình

> "Trong một mini-batch gồm N cặp ảnh và câu, ta tính cosine similarity giữa mọi ảnh với mọi câu, được một ma trận N nhân N — chính là lưới bên phải slide.
>
> Mỗi hàng của ma trận cho qua softmax thì thành một phân phối, em gọi là **p**. Nó có nghĩa là: theo mô hình hiện tại, ảnh này tin rằng câu nào là của nó và với xác suất bao nhiêu.
>
> Trước khi softmax, ta chia similarity cho một tham số nhiệt độ tau. Tau nhỏ thì phân phối nhọn — chênh lệch nhỏ về similarity bị khuếch đại thành chênh lệch lớn về xác suất. Ở đây tau bằng 0.02, tức là nhân similarity với 50, rất nhọn. Hệ quả là nếu có một cặp sai mà mô hình lại chấm điểm cao — ta gọi là **hard negative**, ví dụ hai người khác nhau cùng mặc áo trắng quần đen — thì nó sẽ nhận xác suất lớn và tạo gradient mạnh, buộc mô hình phải xử lý. Đây đúng là trường hợp gây lỗi mà em đã nêu ở phần khó khăn.
>
> Bên cạnh đó là **q**, phân phối nhãn. y bằng 1 nếu ảnh và câu cùng một danh tính, rồi chuẩn hóa cho tổng bằng 1. Em muốn nhấn một điểm tinh tế: nhãn ở đây dựa trên **danh tính**, không phải dựa trên chỉ số cặp. Nên nếu trong batch có nhiều ảnh và nhiều câu của cùng một người, SDM coi tất cả đều là positive. Đây là khác biệt so với loss InfoNCE gốc của CLIP, vốn chỉ coi đường chéo là đúng.
>
> Cuối cùng, SDM tối thiểu hóa KL divergence giữa p và q, theo **cả hai chiều**: ảnh tìm chữ và chữ tìm ảnh.
>
> Câu chốt của slide này là: các loss ghép cặp thông thường chỉ hỏi *cặp đúng có điểm cao không*. SDM hỏi *toàn bộ hình dạng phân phối có đúng không* — tức là vừa đẩy positive lên, vừa chủ động dìm những negative đang nổi lên."

### F. Câu chuyển

> "Hai loss cross-modal này được ghép thêm một loss phân loại danh tính để thành objective hoàn chỉnh."

### G. Nếu bị hỏi

**"SDM khác InfoNCE ở đâu?"**
> Hai điểm. Một, InfoNCE giả định trong batch chỉ có đúng một positive cho mỗi query (đường chéo); SDM cho phép nhiều positive nhờ dùng nhãn danh tính. Hai, InfoNCE là cross-entropy với nhãn one-hot, còn SDM là KL với một **phân phối** nhãn — nên nó khớp cả hình dạng chứ không chỉ nâng một giá trị.

**"Vì sao chọn KL(p‖q) mà không phải KL(q‖p)?"**
> Đây là lựa chọn của tác giả và được giữ nguyên trong code, kèm epsilon `1e-8` để tránh log 0 khi $q$ có phần tử bằng 0. Bài báo không so sánh hai chiều KL, nên em không khẳng định chiều nào tốt hơn.

---

## Slide 15 — II. Proposed Method — Identity Classification Loss

**Thời lượng:** ~60 giây

### A. Trên slide có gì

- **Công thức trên cùng:** `L_ID = ½ [ CE(W f_v, y) + CE(W f_t, y) ]`
- **Khung hình lớn bên trái:** hiện đang là placeholder `PASTE MERMAID FIGURE HERE` → ⚠️ *xem mục "Điểm cần sửa trên deck" ở cuối file*
- **Ba thẻ bên phải:**
  - `SHARED CLASSIFIER` — *the same W is applied to image and text embeddings*
  - `WHAT IT LEARNS` — *identity-discriminative global clusters*
  - `GRADIENT ROUTE` — *classifier W + both CLIP encoders*

### B. Dẫn vào slide

> "SDM lo quan hệ **giữa** hai modality. Còn loss thứ ba này lo cấu trúc **bên trong** mỗi modality."

### C. Giải thích từng khái niệm

- **ID loss / identity classification loss** — coi mỗi danh tính trong tập huấn luyện là một **lớp**, rồi bắt mô hình phân loại. Tập CUHK-PEDES có 11.003 danh tính huấn luyện → 11.003 lớp.
- **$W$ — classifier tuyến tính dùng chung.** Điểm mấu chốt: **cùng một** ma trận $W$ được áp cho **cả** $f^v$ và $f^t$.
  - Nếu dùng hai classifier riêng, mỗi modality sẽ tự hình thành một hệ tọa độ riêng.
  - Dùng chung $W$ nghĩa là cả hai modality phải tham chiếu **cùng một bộ tâm lớp**. Đây là một lực căn chỉnh gián tiếp, bổ sung cho SDM.
- **Class prototype (tâm lớp)** — mỗi hàng của $W$ có thể hiểu là một vector đại diện cho một danh tính. Gradient kéo embedding về phía prototype đúng và đẩy khỏi các prototype khác.
- **Hệ số $\tfrac12$** — code tính CE trung bình trên batch cho từng modality rồi lấy trung bình của hai giá trị. *(`compute_id`: `(criterion(image_logits, labels) + criterion(text_logits, labels)) / 2`.)*
- **`identity-discriminative global clusters`** — ID loss dạy các embedding của cùng một người **tụ lại thành cụm**, tách khỏi cụm của người khác. Nó tác động lên cấu trúc cụm, không trực tiếp tác động lên thứ hạng truy hồi.
- **`GRADIENT ROUTE`** — gradient cập nhật classifier $W$ **và** cả hai CLIP encoder. Nó **không** đi qua interaction encoder hay MLM head. Classifier bị **bỏ khi inference** (11.003 lớp này chỉ có nghĩa trên tập train; tập test là người hoàn toàn khác).

**Điểm phải nói thẳng — và là chỗ ghi điểm về tính phản biện:**

> ID loss là **auxiliary loss**, không phải đóng góp chính của bài báo. Ablation ở slide 20 cho thấy nếu dùng **một mình**, ID loss làm **giảm** Rank-1 (CUHK: 68.19 → 65.33; ICFG: 56.74 → 53.38). Nó chỉ có ích khi không gian đã được căn chỉnh tốt bởi SDM và IRR.

Nói điều này cho thấy bạn đã đọc kỹ ablation chứ không chỉ đọc phần abstract.

### D. Slide này giải quyết vấn đề gì

Nó xử lý phần còn lại của **khó khăn số 1 ở slide 4** — *intra-identity variation*. SDM làm ảnh gần với câu đúng; ID loss làm **các ảnh khác nhau của cùng một người** gần nhau, bất kể góc nhìn hay ánh sáng.

Nói cách khác: SDM là lực **liên modality**, ID là lực **nội modality**. Cần cả hai thì không gian mới có cấu trúc tốt.

### E. Lời thuyết trình

> "Loss thứ ba là ID loss. Ý tưởng đơn giản: coi mỗi danh tính trong tập huấn luyện là một lớp — với CUHK-PEDES là 11.003 lớp — rồi bắt mô hình phân loại.
>
> Điểm đáng chú ý là **cùng một** classifier tuyến tính W được áp cho cả vector ảnh lẫn vector chữ. Nếu dùng hai classifier riêng thì mỗi modality sẽ tự hình thành một hệ tọa độ riêng. Dùng chung W buộc cả hai phải tham chiếu cùng một bộ tâm lớp, nên đây cũng là một lực căn chỉnh gián tiếp.
>
> Về công thức, code tính cross-entropy trung bình trên batch cho từng modality rồi lấy trung bình của hai giá trị — vì vậy có hệ số một phần hai.
>
> Loss này học gì? Nó học các cụm toàn cục phân biệt theo danh tính: gradient kéo mỗi embedding về phía prototype của đúng người và đẩy khỏi các prototype khác. Nó cập nhật classifier cùng cả hai CLIP encoder, nhưng không đi qua interaction encoder hay MLM head. Và classifier bị bỏ khi inference, vì 11.003 lớp này chỉ có nghĩa trên tập train — tập test là những người hoàn toàn khác.
>
> Em muốn nói thẳng một điều: **ID loss là loss bổ trợ, không phải đóng góp chính của bài báo**. Ablation cho thấy nếu dùng một mình, nó thậm chí làm Rank-1 giảm — trên CUHK từ 68.19 xuống 65.33. Nó chỉ phát huy khi không gian đã được căn chỉnh tốt bởi SDM và IRR. Em sẽ quay lại con số này ở phần ablation."

### F. Câu chuyển

> "Đã đủ ba loss. Giờ ta xem chúng được ghép lại thế nào, và điều gì xảy ra khi chuyển từ huấn luyện sang triển khai."

---

## Slide 16 — II. Proposed Method — Training vs. Inference

**Thời lượng:** ~75 giây — **slide chốt của phần phương pháp**

### A. Trên slide có gì

- **Công thức trên cùng:** `L = L_IRR + L_SDM + L_ID`
- **Thẻ `TRAIN`:** CLIP dual encoder / + IRR interaction encoder / + MLM head / + SDM and ID classifier / → *end-to-end local interaction learning*
- **Thẻ `INFERENCE`:** Only the two encoders remain / Precomputed gallery embeddings / One cosine score per image–text pair / No interaction module required / → *efficient global retrieval*
- **Thanh đỏ dưới cùng:** *Fine-grained learning → efficient global retrieval*

### B. Dẫn vào slide

> "Đây là slide mà em muốn khán giả nhớ nhất trong phần phương pháp, vì nó chính là luận điểm của cả bài báo."

### C. Giải thích từng khái niệm

**1. Tổng loss là PHÉP CỘNG, không phải trung bình cộng**

$$\mathcal L = \mathcal L_{\mathrm{IRR}} + \mathcal L_{\mathrm{SDM}} + \mathcal L_{\mathrm{ID}}$$

Đây là Equation (7) của bài báo, và code làm đúng như vậy:

```python
ret = model(batch)
total_loss = sum([v for k, v in ret.items() if "loss" in k])
total_loss.backward()
```

Mặc định `loss_names='sdm+id+mlm'`, `mlm_loss_weight=1.0`, `id_loss_weight=1.0` — tức là **không có trọng số nào khác 1**. Từng loss đã có phép trung bình **bên trong** nó rồi (trung bình trên batch, trên các vị trí bị che), nên việc cộng ba scalar ở ngoài là hợp lý.

*(Đây là câu hỏi hay bị hỏi, nên chuẩn bị sẵn.)*

**2. Gradient được cộng tại các tham số dùng chung**

Với tham số của image encoder $\theta_v$:

$$\nabla_{\theta_v}\mathcal L = \nabla_{\theta_v}\mathcal L_{\mathrm{IRR}} + \nabla_{\theta_v}\mathcal L_{\mathrm{SDM}} + \nabla_{\theta_v}\mathcal L_{\mathrm{ID}}$$

Không phải backward ba lần với ba optimizer step. Autograd dựng **một** đồ thị tính toán chung, cộng ba scalar, rồi backward **một lần**.

**3. Bảng định tuyến gradient — nói bảng này nếu có thời gian, nó rất thuyết phục**

| Tham số | IRR/MLM | SDM | ID | Còn khi inference? |
|---|:---:|:---:|:---:|:---:|
| Image encoder (ViT) | ✓ | ✓ | ✓ | **Có** |
| Text encoder | ✓ | ✓ | ✓ | **Có** |
| Interaction encoder + MLM head | ✓ | – | – | Không |
| Identity classifier $W$ | – | – | ✓ | Không |
| Temperature $\tau = 0.02$ | – | cố định | – | Không |

**Đọc bảng theo cột "Còn khi inference":** hai hàng đầu nhận gradient từ **cả ba** loss và **được giữ lại**. Ba hàng dưới bị bỏ. Nghĩa là toàn bộ tri thức từ ba nhiệm vụ đã được **dồn vào đúng hai khối sống sót**.

**4. Vì sao bỏ nhánh phụ mà không mất kiến thức — đây là lập luận quan trọng nhất**

> Interaction encoder và MLM head đóng vai trò như một **giàn giáo huấn luyện**. Nhiệm vụ của chúng là tạo ra gradient. Gradient đó **đã** chảy vào hai encoder và **đã** thay đổi trọng số của chúng. Khi tháo giàn giáo đi, trọng số đã thay đổi vẫn còn nguyên đó.

Một cách nói khác dễ hình dung hơn:
> Giống như học sinh làm bài tập khó có hướng dẫn. Khi đi thi thì không mang hướng dẫn theo, nhưng năng lực có được từ quá trình đó thì vẫn còn.

**5. Đóng góp về mặt hệ thống**

- Train nặng: hai encoder + interaction encoder + MLM head + classifier, câu chạy hai lượt.
- Inference gọn: đúng hai encoder + một phép cosine.
- **So với CLIP dual encoder, chi phí inference không tăng một chút nào**, nhưng độ chính xác tăng 5–7 điểm Rank-1.
- Lưu ý trung thực: bài báo **chưa** benchmark một vector database thật (chưa đo ANN index, footprint, latency end-to-end). Nhưng kiến trúc thì đã hoàn toàn tương thích với mô hình đó.

### D. Slide này giải quyết vấn đề gì

Slide này **đóng vòng tròn của cả bài trình bày**:

- Slide 3 đặt ra ràng buộc của cơ sở dữ liệu: gallery phải mã hóa trước được.
- Slide 4 đặt ra mâu thuẫn: cần chi tiết nhưng cũng cần vector toàn cục.
- Slide 5–6 cho thấy các hướng cũ đều phải hy sinh một bên.
- **Slide 16 cho thấy IRRA không phải hy sinh bên nào.**

Đây chính là chỗ để bạn phát biểu lại câu tóm tắt: *"đưa chi tiết vào quá trình học, không đưa chi phí của chi tiết vào quá trình truy hồi"*.

### E. Lời thuyết trình

> "Đây là slide chốt phần phương pháp.
>
> Trước hết, về tổng loss: ba loss được **cộng** trực tiếp, không phải trung bình cộng. Đây là Equation 7 của bài báo và code làm đúng như vậy — vòng huấn luyện cộng tất cả các scalar loss rồi gọi backward đúng một lần. Trọng số mặc định của MLM và ID đều bằng một. Từng loss đã có phép trung bình bên trong nó rồi, nên cộng ở ngoài là hợp lý.
>
> Vì backward chỉ gọi một lần trên một đồ thị chung, nên tại các tham số dùng chung, đạo hàm của tổng bằng tổng các đạo hàm. Cụ thể, image encoder và text encoder nhận **đồng thời ba tín hiệu**: quan hệ token cục bộ từ IRR, phân phối cross-modal toàn cục từ SDM, và tính phân biệt danh tính từ ID. Các head riêng thì chỉ nhận gradient từ loss tương ứng: interaction encoder và MLM head chỉ do IRR cập nhật, classifier chỉ do ID.
>
> Và đây là điểm mấu chốt. Nhìn hai cột trên slide: khi train ta có đầy đủ năm khối. Khi inference, ta bỏ interaction encoder, bỏ MLM head, bỏ ID classifier. **Chỉ còn đúng hai encoder và một phép cosine.**
>
> Vậy có mất kiến thức không? Không. Em xin dùng một hình ảnh: các nhánh phụ đóng vai trò như **giàn giáo huấn luyện**. Nhiệm vụ của chúng là tạo ra gradient, và gradient đó **đã** chảy vào hai encoder, **đã** thay đổi trọng số của chúng. Khi tháo giàn giáo đi thì trọng số đã thay đổi vẫn còn nguyên. Giống như học sinh làm bài tập khó có hướng dẫn — đi thi không mang hướng dẫn theo, nhưng năng lực thì vẫn còn.
>
> Về mặt hệ thống, đây chính là đóng góp: **train nặng nhưng inference gọn**. So với CLIP dual encoder thì chi phí truy hồi không tăng một chút nào, trong khi Rank-1 tăng 5 đến 7 điểm. Ta có thể tiền tính toán toàn bộ embedding của gallery và đưa vào một hệ thống vector search, đúng như pipeline ở slide 3.
>
> Em cũng xin nói trung thực: bài báo **chưa** benchmark một vector database thật — chưa đo chỉ mục ANN, chưa đo footprint hay latency end-to-end. Nhưng kiến trúc thì đã hoàn toàn tương thích.
>
> Tóm lại một câu: **IRRA đưa chi tiết vào quá trình học, nhưng không đưa chi phí của chi tiết đó vào quá trình truy hồi.**"

### F. Câu chuyển

> "Đó là toàn bộ phương pháp. Tiếp theo, tác giả kiểm chứng nó trên ba bộ dữ liệu."

### G. Nếu bị hỏi

**"Tổng loss có phải trung bình cộng ba loss không?"**
> Không. Equation (7) và vòng huấn luyện đều dùng **tổng**. Các phép trung bình nằm **bên trong** từng loss. Nếu chia tổng cho 3 thì hướng gradient giữ nguyên nhưng độ lớn giảm ba lần — đó không phải implementation được báo cáo và có thể làm thay đổi động học tối ưu.

**"Tại sao không đặt trọng số cho từng loss?"**
> Code có sẵn `mlm_loss_weight` và `id_loss_weight`, nhưng mặc định đều bằng 1.0 và bài báo không báo cáo kết quả tinh chỉnh trọng số. Đây là một hướng thử nghiệm bỏ ngỏ.

---

# PHẦN THỰC NGHIỆM VÀ KẾT QUẢ

---

## Slide 17 — III. Experiments — Three Benchmarks

**Thời lượng:** ~60 giây

### A. Trên slide có gì

- **Bảng ba dataset** với số danh tính / ảnh / mô tả
- **Thẻ `IDENTITY-DISJOINT SPLIT`:** *No identity appears in both training and test sets*
- Ba nhãn: `CUHK: first benchmark` / `ICFG: large test gallery` / `RSTP: multi-camera`
- **Thanh dưới:** *Test = generalization to unseen identities*

### B. Dẫn vào slide

> "Chuyển sang phần kiểm chứng. Bài báo đánh giá trên ba bộ dữ liệu, và mỗi bộ được chọn để kiểm tra một khía cạnh khác nhau."

### C. Giải thích từng khái niệm

**Số liệu để đối chiếu (nếu bảng trên slide bị hỏi chi tiết):**

| Dataset | Danh tính | Ảnh | Mô tả | Đặc điểm |
|---|---:|---:|---:|---|
| CUHK-PEDES | 13.003 | 40.206 | 80.412 | 2 mô tả/ảnh; benchmark **đầu tiên** của bài toán |
| ICFG-PEDES | 4.102 | 54.522 | 54.522 | 1 mô tả/ảnh; **test gallery lớn** — 19.848 cặp |
| RSTPReid | 4.101 | 20.505 | 41.010 | 15 camera; 5 ảnh/danh tính; 2 mô tả/ảnh |

Split chi tiết (chỉ nói nếu được hỏi):
- CUHK: train 11.003 danh tính / 34.054 ảnh / 68.108 mô tả; val và test mỗi tập 1.000 danh tính.
- ICFG: train/test = 3.102 / 1.000 danh tính, tương ứng 34.674 / 19.848 cặp.
- RSTPReid: train/val/test = 3.701 / 200 / 200 danh tính.

**Identity-disjoint split — khái niệm quan trọng nhất của slide:**

- Tập train và tập test **không chia sẻ bất kỳ danh tính nào**. Một người đã xuất hiện khi huấn luyện sẽ **không** xuất hiện khi kiểm thử.
- **Vì sao điều này quan trọng?** Vì nó loại bỏ khả năng mô hình "học thuộc" danh tính. Mô hình không thể ghi nhớ "người số 47 trông thế này". Nó buộc phải học **cách ánh xạ thuộc tính ngôn ngữ sang đặc trưng thị giác** một cách tổng quát.
- Hệ quả: kết quả test đo đúng **khả năng khái quát hóa sang người chưa từng thấy** — đúng với tình huống sử dụng thực tế.

**Vì sao ba bộ chứ không phải một:**
- CUHK-PEDES — chuẩn so sánh lịch sử, mọi phương pháp trước đều báo cáo trên đây.
- ICFG-PEDES — gallery test lớn hơn nhiều, nên khó hơn; kiểm tra mô hình có chịu được quy mô không.
- RSTPReid — 15 camera, kiểm tra độ bền với thay đổi góc nhìn và điều kiện chụp.

### D. Slide này giải quyết vấn đề gì

Slide này **thiết lập độ tin cậy** cho toàn bộ phần kết quả sắp tới. Nếu chỉ đánh giá trên một dataset, khán giả có quyền nghi ngờ là may mắn hoặc overfit. Ba dataset với ba đặc điểm khác nhau, cộng với split theo danh tính, làm cho kết luận ở slide 19–20 đáng tin hơn nhiều.

### E. Lời thuyết trình

> "Bài báo đánh giá trên ba benchmark.
>
> **CUHK-PEDES** là bộ dữ liệu đầu tiên cho bài toán này và lớn nhất về số mô tả — hơn 80 nghìn câu cho 13 nghìn danh tính, mỗi ảnh có hai mô tả. Đây là chuẩn so sánh lịch sử, mọi phương pháp trước đều báo cáo trên đây.
>
> **ICFG-PEDES** có nhiều ảnh hơn nhưng chỉ một câu cho mỗi ảnh, và quan trọng hơn là gallery test lớn hơn nhiều — gần 20 nghìn cặp. Nên nó khó hơn, dùng để kiểm tra mô hình có chịu được quy mô không.
>
> **RSTPReid** nhấn mạnh multi-camera: 15 camera, mỗi danh tính có năm ảnh từ các camera khác nhau. Nó kiểm tra độ bền với thay đổi góc nhìn và điều kiện chụp.
>
> Điểm em muốn nhấn nhất ở slide này là **identity-disjoint split**: tập train và tập test không chia sẻ bất kỳ danh tính nào. Một người đã xuất hiện khi huấn luyện sẽ không xuất hiện khi kiểm thử.
>
> Điều này rất quan trọng vì nó loại bỏ khả năng mô hình học thuộc danh tính. Mô hình không thể ghi nhớ 'người số 47 trông thế này'. Nó buộc phải học cách ánh xạ thuộc tính ngôn ngữ sang đặc trưng thị giác một cách tổng quát. Nên con số ở các slide sau đo đúng khả năng khái quát hóa sang người chưa từng thấy — tức là đúng với tình huống sử dụng thật."

### F. Câu chuyển

> "Vì đây là bài toán xếp hạng chứ không phải phân loại, accuracy thông thường không đủ. Tác giả dùng ba họ chỉ số."

---

## Slide 18 — III. Experiments — Metrics and Training Setup

**Thời lượng:** ~75 giây

### A. Trên slide có gì

- **Ba thẻ metric:**
  - `RANK-k` — *At least one correct image appears in Top-k*
  - `mAP` — *Ranking quality across all relevant images*
  - `mINP` — *Position of the hardest / last relevant image*
- **Thẻ `IMPLEMENTATION`** hai cột: CLIP ViT-B/16 • 384×128 • ≤77 tokens • Adam • 60 epochs ‖ LR 1e−5 • warm-up 5 epochs • new modules 5e−5 • τ=0.02 • RTX 3090
- **Dòng chốt:** *Higher is better for all metrics*

### B. Dẫn vào slide

> "Ba chỉ số này đo ba thứ khác nhau, và khoảng cách giữa chúng sẽ nói lên điều thú vị ở slide hạn chế. Em xin giải thích bằng một ví dụ cụ thể."

### C. Giải thích từng khái niệm

**Cách giải thích hiệu quả nhất: dựng một ví dụ và dùng chung cho cả ba chỉ số.**

> Giả sử một truy vấn có **3 ảnh đúng** trong gallery. Mô hình trả về danh sách xếp hạng, và ba ảnh đúng nằm ở vị trí **1, 4 và 20**.

- **Rank-k** — *có ít nhất một ảnh đúng trong Top-k hay không*. Chỉ trả lời có/không.
  - Rank-1 = **đạt** (ảnh đúng ở vị trí 1).
  - Rank-5 = **đạt**, Rank-10 = **đạt**.
  - Đây là chỉ số **thân thiện với người dùng nhất**: người dùng thường chỉ nhìn trang kết quả đầu tiên. Nhưng nó **bỏ qua** việc còn hai ảnh đúng nữa ở đâu.
- **mAP (mean Average Precision)** — quan tâm **tất cả** ảnh đúng và vị trí của chúng. Đẩy được cả ba ảnh đúng lên cao thì mAP cao; nếu chỉ ảnh đầu đúng còn hai ảnh kia rất xa thì mAP thấp dù Rank-1 vẫn đạt.
  - → **Vì vậy mAP luôn thấp hơn Rank-1 nhiều.** Đừng để khán giả hiểu nhầm đó là mô hình kém.
- **mINP (mean Inverse Negative Penalty)** — chỉ quan tâm **ảnh đúng nằm xa nhất**, tức vị trí 20 trong ví dụ. Nó đo *phải duyệt bao xa mới gom đủ tất cả ảnh đúng*.
  - Đây là chỉ số **khắc nghiệt nhất**, và thường thấp hơn hẳn hai chỉ số kia.
  - Ý nghĩa thực tế: nếu ứng dụng cần **tìm đủ mọi lần xuất hiện** của một người (ví dụ dựng lại lộ trình di chuyển qua nhiều camera) thì mINP mới là chỉ số đáng quan tâm, chứ không phải Rank-1.
  - ⚠️ **Ghi nhớ:** mINP của IRRA trên ICFG chỉ là **7.93**. Con số này sẽ quay lại ở slide 22 (Hạn chế).

**Phần implementation — nói lướt, chỉ nhấn ba điểm:**

- **`τ = 0.02`** — đã giải thích ở slide 14, chỉ nhắc lại là nó **cố định**, không phải tham số học được.
- **Learning rate phân tầng:** backbone CLIP đã pre-train dùng LR `1e−5` (nhỏ, để không phá trọng số tốt sẵn có); các module mới khởi tạo ngẫu nhiên — interaction encoder, MLM head, classifier — dùng LR `5e−5`, **gấp 5 lần**. Đây là thực hành chuẩn khi fine-tune.
- **Một GPU RTX 3090 duy nhất** — đáng nhắc: đây là quy mô mà một nhóm sinh viên có thể tái lập được.
- *(Bổ sung không có trên slide: augmentation gồm lật ngang, random crop có padding, random erasing; scheduler cosine decay; warm-up tuyến tính 5 epoch từ `1e−6`. Repository chính thức chạy `batch_size = 64`, còn phần implementation details của bài báo không nêu batch size.)*

### D. Slide này giải quyết vấn đề gì

Hai việc:

1. **Dạy khán giả cách đọc bảng kết quả** ở slide 19–20. Không có slide này, con số mAP 38.06 sẽ bị hiểu nhầm là kém.
2. **Cài sẵn bằng chứng cho phần phản biện.** Khi bạn nói ở slide 22 rằng "mINP trên ICFG chỉ 7.93, hard positive vẫn bị xếp rất xa", khán giả đã có sẵn khái niệm để hiểu ngay.

### E. Lời thuyết trình

> "Em xin giải thích ba chỉ số bằng một ví dụ chung. Giả sử một truy vấn có ba ảnh đúng trong gallery, và mô hình xếp chúng ở vị trí một, bốn và hai mươi.
>
> **Rank-k** chỉ hỏi: có ít nhất một ảnh đúng trong Top-k hay không. Ở đây Rank-1 đạt, Rank-5 đạt, Rank-10 đạt. Đây là chỉ số thân thiện với người dùng nhất, vì người dùng thường chỉ nhìn trang kết quả đầu. Nhưng nó bỏ qua việc còn hai ảnh đúng nữa nằm đâu.
>
> **mAP** quan tâm tất cả ảnh đúng và vị trí của chúng. Nếu đẩy được cả ba lên cao thì mAP cao; nếu chỉ ảnh đầu đúng còn hai ảnh kia rất xa thì mAP thấp. Vì vậy mAP luôn thấp hơn Rank-1 khá nhiều — em nói trước để lát nữa nhìn bảng kết quả không bị hiểu nhầm.
>
> **mINP** khắc nghiệt nhất: nó chỉ quan tâm ảnh đúng nằm **xa nhất**, tức vị trí hai mươi trong ví dụ. Nó đo xem phải duyệt bao xa mới gom đủ mọi ảnh đúng. Chỉ số này quan trọng khi ứng dụng cần tìm đủ mọi lần xuất hiện của một người, ví dụ dựng lại lộ trình di chuyển qua nhiều camera. Em xin nhớ trước một con số: mINP của IRRA trên ICFG chỉ là 7.93 — em sẽ quay lại ở phần hạn chế.
>
> Cả ba chỉ số đều càng cao càng tốt.
>
> Về thiết lập huấn luyện, em chỉ nhấn ba điểm. Tau bằng 0.02 và **cố định**, không phải tham số học được. Learning rate được chia tầng: backbone CLIP đã pre-train dùng 1e−5 để không phá trọng số tốt sẵn có, còn các module mới khởi tạo ngẫu nhiên dùng 5e−5, gấp năm lần. Và toàn bộ chỉ chạy trên **một GPU RTX 3090** — tức là quy mô mà một nhóm sinh viên hoàn toàn có thể tái lập."

### F. Câu chuyển

> "Với thiết lập đó, IRRA đạt kết quả thế nào so với baseline CLIP và phương pháp tốt nhất trước đó?"

---

## Slide 19 — III. Results — State-of-the-Art Comparison (2023)

**Thời lượng:** ~80 giây

### A. Trên slide có gì

- **Biểu đồ cột nhóm** Rank-1 trên ba dataset, ba màu: `CLIP baseline` / `CFine` / `IRRA`
  - CUHK: 68.19 / 69.57 / **73.38**
  - ICFG: 56.74 / 60.83 / **63.46**
  - RSTP: 54.05 / 50.55 / **60.20**
- **Ba thẻ mức tăng so với CFine:** `+3.81` / `+2.63` / `+9.65`

### B. Dẫn vào slide

> "Slide này chỉ hiển thị Rank-1, vì đó là chỉ số dễ so sánh nhất. Số đầy đủ em để ở appendix."

### C. Giải thích từng khái niệm

- **CLIP baseline** — chính CLIP ViT-B/16 được fine-tune trực tiếp cho bài toán này, **không có** IRR, **không có** SDM. Đây là mốc để đo xem đóng góp của bài báo đáng giá bao nhiêu.
- **CFine** — phương pháp tốt nhất trước đó được bài báo đem ra so sánh (prior best).
- **IRRA** — mô hình đầy đủ.

**Ba quan sát cần nói, theo đúng thứ tự tăng dần độ thú vị:**

**1. IRRA thắng trên cả ba dataset.** Rank-1 đạt 73.38 / 63.46 / 60.20. So với CFine: **+3.81 / +2.63 / +9.65** điểm phần trăm.

**2. Mức tăng trên RSTPReid lớn bất thường: +9.65 điểm.** Nên chỉ ra và giải thích, vì nó sẽ bị hỏi:
> RSTPReid là bộ multi-camera, biến thiên trong cùng danh tính lớn nhất. Đây đúng là trường hợp mà đặc trưng toàn cục thô dễ thất bại nhất và chi tiết cục bộ có giá trị nhất — nên thành phần IRR phát huy mạnh nhất ở đây.

**3. Quan sát thú vị nhất — CLIP baseline đã rất mạnh.** Trên RSTPReid, CLIP baseline đạt **54.05**, còn **cao hơn** CFine (50.55) — dù CFine là công trình chuyên biệt cho bài toán này.
> **Ý nghĩa:** điều này ủng hộ lập luận ở slide 6 rằng pre-training **chung** trên cặp ảnh–văn bản có giá trị hơn việc ghép hai backbone được pre-train **riêng** cho từng modality.

**4. Do đó, phép so sánh công bằng nhất là IRRA so với CLIP baseline**, vì cả hai cùng xuất phát từ cùng một điểm. Mức tăng: **+5.19 / +6.72 / +6.15** điểm Rank-1. Đây mới đúng là phần đóng góp của IRR + SDM.

**Cách phát biểu chính xác về "SOTA" — rất quan trọng:**
> Nói **"đạt state of the art tại thời điểm công bố, so với các baseline được đánh giá trong bài báo"**.
> **Đừng** nói "hiện nay vẫn là tốt nhất" — bài báo từ 2023 và lĩnh vực này thay đổi nhanh.

**Số đầy đủ, chỉ dùng khi được hỏi:**

| Dataset | R1 | R5 | R10 | mAP | mINP |
|---|---:|---:|---:|---:|---:|
| CUHK-PEDES | 73.38 | 89.93 | 93.71 | 66.13 | 50.24 |
| ICFG-PEDES | 63.46 | 80.25 | 85.82 | 38.06 | 7.93 |
| RSTPReid | 60.20 | 81.30 | 88.20 | 47.17 | 25.28 |

### D. Slide này giải quyết vấn đề gì

Đây là **bằng chứng chính** cho toàn bộ bài báo: phương pháp có hiệu quả thật, và hiệu quả **nhất quán** trên ba bộ dữ liệu có đặc điểm khác nhau.

Nhưng slide này **chưa** trả lời được *thành phần nào tạo ra hiệu quả đó* — đó là lý do phải có slide 20.

### E. Lời thuyết trình

> "Biểu đồ này so sánh Rank-1 của ba mô hình trên ba dataset. Màu đầu là CLIP baseline — chính CLIP fine-tune trực tiếp, không có IRR, không có SDM. Màu giữa là CFine, phương pháp tốt nhất trước đó. Màu cuối là IRRA.
>
> **Quan sát thứ nhất:** IRRA thắng trên cả ba, Rank-1 lần lượt là 73.38, 63.46 và 60.20. So với CFine, mức tăng là 3.81, 2.63 và 9.65 điểm phần trăm.
>
> **Quan sát thứ hai:** mức tăng trên RSTPReid lớn bất thường, gần mười điểm. Em nghĩ điều này hợp lý: RSTPReid là bộ multi-camera, biến thiên trong cùng một danh tính lớn nhất. Đây đúng là trường hợp mà đặc trưng toàn cục thô dễ thất bại nhất và chi tiết cục bộ có giá trị nhất, nên thành phần IRR phát huy mạnh nhất.
>
> **Quan sát thứ ba, mà em thấy thú vị nhất:** CLIP baseline đã rất mạnh. Trên RSTPReid, nó đạt 54.05 — **cao hơn cả CFine** là 50.55, dù CFine là công trình chuyên biệt cho bài toán này. Điều này ủng hộ đúng lập luận ở slide về CLIP: pre-training chung trên cặp ảnh và văn bản có giá trị hơn việc ghép hai backbone được pre-train riêng cho từng modality.
>
> Vì vậy em cho rằng **phép so sánh công bằng nhất là IRRA với CLIP baseline**, vì cả hai cùng xuất phát điểm. Mức tăng khi đó là 5.19, 6.72 và 6.15 điểm — và đây mới đúng là phần đóng góp của IRR cộng SDM.
>
> Em xin phát biểu chính xác: đây là **state of the art tại thời điểm công bố, so với các baseline được đánh giá trong bài báo**. Bài báo từ năm 2023 và lĩnh vực này thay đổi rất nhanh, nên em không khẳng định hiện nay vẫn là tốt nhất."

### F. Câu chuyển

> "Kết quả tổng thể tốt vẫn chưa chứng minh thành phần nào thực sự cần thiết. Câu trả lời nằm ở ablation."

---

## Slide 20 — III. Results — Ablation: IRR and SDM

**Thời lượng:** ~85 giây

### A. Trên slide có gì

- **Biểu đồ cột** mức tăng Rank-1 so với CLIP baseline, ba nhóm màu `+ SDM` / `+ IRR` / `Full IRRA`:

| Thành phần | CUHK | ICFG | RSTP |
|---|---:|---:|---:|
| `+ SDM` | +2.23 | +3.71 | +3.15 |
| `+ IRR` | +3.04 | +4.22 | +3.85 |
| `Full IRRA` | **+5.19** | **+6.72** | **+6.15** |

- **Cột `TAKEAWAY` bên phải:** `IRR > SDM` (*R1 gain: +3.04 to +4.22*) / `FULL MODEL WINS` (*Complementary gains*) / `ID LOSS` (*Alone, it may reduce R1*) / `CMPM` (*Weaker than SDM*)

### B. Dẫn vào slide

> "Ablation là phần em thấy trung thực nhất của bài báo, vì nó cũng cho thấy một thành phần **không** hiệu quả khi đứng một mình."

### C. Giải thích từng khái niệm

- **Ablation study (nghiên cứu cắt bỏ)** — bật/tắt từng thành phần để đo đóng góp riêng của nó. Đây là cách duy nhất để phân biệt *"mô hình tốt"* với *"ý tưởng tốt"*.
- **Mọi con số trên biểu đồ là mức TĂNG so với CLIP baseline**, không phải Rank-1 tuyệt đối. Nói rõ điều này, nếu không khán giả sẽ tưởng mô hình chỉ đạt 5 điểm.

**Bốn kết luận, theo đúng bốn thẻ TAKEAWAY:**

**1. `IRR > SDM` — IRR đóng góp nhiều hơn SDM.**
+3.04 / +4.22 / +3.85 so với +2.23 / +3.71 / +3.15. Nhất quán trên cả ba dataset.
> **Ý nghĩa:** đóng góp mang tên bài báo (Implicit Relation Reasoning) đúng là đóng góp mạnh nhất. Tên bài báo không bị "thổi".

**2. `FULL MODEL WINS` — hai thành phần bổ sung cho nhau.**
Nếu chúng học cùng một thứ, mô hình đầy đủ sẽ chỉ bằng thành phần mạnh nhất (~+4.22). Thực tế đạt +6.72.
> **Ý nghĩa:** IRR và SDM học hai thứ **khác nhau** — đúng như phân tích ở slide 12 và 14: IRR dạy mô hình *nhìn vào đâu*, SDM dạy mô hình *sắp xếp mọi thứ so với nhau*.

**3. `ID LOSS — Alone, it may reduce R1`.** Đây là chỗ nên dừng lại và nói kỹ:
> Dùng **một mình**, ID loss làm Rank-1 **giảm**: CUHK từ 68.19 xuống **65.33**, ICFG từ 56.74 xuống **53.38**.
>
> **Vì sao?** ID loss tối ưu bài toán **phân loại**, không tối ưu bài toán **xếp hạng cross-modal**. Nó gom cụm theo danh tính trong từng modality, nhưng không đảm bảo cụm ảnh và cụm chữ của cùng một người trùng lên nhau. Nó chỉ có ích khi đã có một lực căn chỉnh khác (SDM, IRR) giữ hai modality lại với nhau.
>
> **Vì vậy đừng kể câu chuyện "mọi loss đều độc lập có lợi".** Nói thẳng điều này cho thấy bạn đã đọc kỹ bảng, và đó là điểm cộng khi phản biện.

**4. `CMPM — Weaker than SDM`.**
CMPM (Cross-Modal Projection Matching) là loss được dùng phổ biến trong các công trình trước. Trong cấu hình CLIP này, CMPM trên CUHK chỉ đạt **59.31**, trong khi SDM đạt **70.42**.
> **Ý nghĩa:** đây là bằng chứng trực tiếp cho động cơ thiết kế SDM — không phải "thay loss cho khác người", mà vì loss cũ thực sự kém trong cấu hình này.

### D. Slide này giải quyết vấn đề gì

Slide 19 chứng minh **mô hình tốt**. Slide 20 chứng minh **ý tưởng tốt** — và đó là hai chuyện khác nhau.

Cụ thể, nó xác nhận đúng hai luận điểm bạn đã xây từ đầu bài:
- IRR (slide 12–13) thực sự là thành phần đóng góp mạnh nhất.
- IRR và SDM giải quyết hai vấn đề khác nhau, nên cộng lại thì lợi ích cộng dồn.

### E. Lời thuyết trình

> "Ablation là bật tắt từng thành phần để đo đóng góp riêng. Em lưu ý mọi con số trên biểu đồ là **mức tăng** so với CLIP baseline, không phải Rank-1 tuyệt đối.
>
> **Thứ nhất, IRR đóng góp nhiều hơn SDM** trên cả ba dataset — khoảng 3 đến 4.2 điểm so với 2.2 đến 3.7 điểm. Tức là đóng góp mang tên bài báo đúng là đóng góp mạnh nhất, tên bài báo không bị thổi.
>
> **Thứ hai, mô hình đầy đủ tăng 5.19 đến 6.72 điểm.** Đây là con số đáng chú ý: nếu IRR và SDM học cùng một thứ thì mô hình đầy đủ sẽ chỉ xấp xỉ thành phần mạnh nhất, tức khoảng 4.2. Thực tế nó đạt 6.72, nghĩa là hai thành phần học hai thứ **khác nhau** và bổ sung cho nhau — đúng như em đã phân tích: IRR dạy mô hình nhìn vào đâu, còn SDM dạy mô hình sắp xếp mọi thứ so với nhau.
>
> **Thứ ba, và em muốn nói thẳng điều này:** ID loss dùng một mình lại làm Rank-1 **giảm**. Trên CUHK từ 68.19 xuống 65.33, trên ICFG từ 56.74 xuống 53.38. Lý do là ID loss tối ưu bài toán phân loại chứ không tối ưu bài toán xếp hạng cross-modal — nó gom cụm theo danh tính trong từng modality, nhưng không đảm bảo cụm ảnh và cụm chữ của cùng một người trùng lên nhau. Nó chỉ có ích khi đã có một lực căn chỉnh khác giữ hai modality lại. Vì vậy em không kể câu chuyện rằng mọi loss đều độc lập có lợi.
>
> **Thứ tư**, CMPM — loss phổ biến trong các công trình trước — cũng yếu trong cấu hình CLIP này: trên CUHK chỉ 59.31, trong khi SDM đạt 70.42. Đây là bằng chứng trực tiếp cho lý do tác giả thiết kế SDM."

### F. Câu chuyển

> "Ngoài độ chính xác, bài báo còn đo chi phí của module tương tác và đưa ra ví dụ truy hồi cụ thể."

---

## Slide 21 — III. Results — Efficiency and Qualitative Results

**Thời lượng:** ~75 giây

### A. Trên slide có gì

- **Thẻ `INTERACTION MODULE`** với bảng so sánh ba module; chú thích *~3× faster than merged attention*
- **Thẻ:** *Why does IRRA perform better?* — *IRR exploits subtle discriminative attributes: clothing • colors • shoes • bags*; nhãn đỏ *Interaction module removed at inference*
- **Dải dưới:** một truy vấn cụ thể, hai hàng kết quả `Baseline` và `IRRA` (Figure 5)

### B. Dẫn vào slide

> "Slide này có hai nửa: nửa trên trả lời *có đắt không*, nửa dưới trả lời *tốt hơn ở chỗ nào*."

### C. Giải thích từng khái niệm

**Nửa trên — hiệu quả tính toán (Table 5, trên CUHK-PEDES):**

| Module | Tham số | Time | Rank-1 |
|---|---:|---:|---:|
| Co-attention | 33.62M | 24.30 ms | 73.28 |
| Merged attention | 12.61M | 19.20 ms | 73.21 |
| **IRRA (one-way)** | 13.66M | **6.42 ms** | **73.38** |

Ba điều rút ra:
1. **Rank-1 của ba module gần như bằng nhau** (73.21 – 73.38). Nghĩa là *kiểu* module tương tác không quan trọng lắm; điều quan trọng là **có** tương tác.
2. **Nhưng chi phí thì chênh lệch rất lớn.** IRRA nhanh hơn merged attention khoảng 3 lần và nhanh hơn co-attention khoảng 3,8 lần, với số tham số gần bằng merged attention.
3. → **Kết luận thiết kế:** chọn module rẻ nhất là lựa chọn đúng, vì không mất gì về độ chính xác.

**Cảnh báo cần nói để tránh bị vặn:**
> Bài báo **không mô tả đầy đủ giao thức đo thời gian** ở Table 5. Nên phải hiểu đây là **so sánh nội bộ giữa ba module trong cùng điều kiện**, không phải latency end-to-end của một hệ thống production.

**Và một điều dễ gây hiểu nhầm, phải nói rõ:**
> Thời gian 6.42 ms này là chi phí **trong lúc huấn luyện**. Khi inference, module này **bị bỏ hoàn toàn**, nên chi phí thực tế khi truy hồi là **0**. Đây là điều nhãn đỏ trên slide muốn nói.

**Nửa dưới — kết quả định tính (Figure 5):**

- Mỗi truy vấn có hai hàng: hàng trên là baseline, hàng dưới là IRRA.
- Quy ước màu khung trong hình gốc: khung **xanh** = kết quả đúng, khung **đỏ** = sai.
- Trong câu truy vấn, các cụm được **tô cam** là thuộc tính phân biệt: *green pants*, *black book bag*, *blue tennis shoes*.
- **Cách đọc:** IRRA đưa được nhiều ảnh đúng lên Top-10 hơn, và các ảnh nó chọn đúng thường khớp chính xác ở những cụm được tô cam — tức là đúng những chi tiết nhỏ mà slide 4 đã nêu là nguồn gốc khó khăn, và slide 12 đã nêu là mục tiêu của IRR.
- → Đây là **bằng chứng định tính** cho cơ chế, bổ sung cho bằng chứng định lượng ở slide 19–20.

### D. Slide này giải quyết vấn đề gì

Nó **khép lại vòng lập luận về chi phí** — chủ đề xuyên suốt của bài nói và là lý do bài báo này phù hợp với học phần cơ sở dữ liệu:

- Slide 3 nêu ràng buộc chi phí.
- Slide 5–6 cho thấy các hướng khác vi phạm ràng buộc đó.
- Slide 16 khẳng định IRRA không vi phạm.
- **Slide 21 đưa số đo cụ thể để chứng minh.**

Đồng thời nửa dưới cho khán giả thấy tận mắt mô hình đang khai thác chi tiết gì — biến một cơ chế trừu tượng thành thứ nhìn được.

### E. Lời thuyết trình

> "Slide này có hai nửa.
>
> **Nửa trên là chi phí.** Bảng so sánh ba kiểu module tương tác. Điều đầu tiên đáng chú ý: Rank-1 của cả ba gần như bằng nhau, từ 73.21 đến 73.38. Nghĩa là **kiểu** module tương tác không quan trọng lắm — điều quan trọng là **có** tương tác.
>
> Nhưng chi phí thì chênh lệch rất lớn. Module của IRRA có số tham số gần bằng merged attention nhưng thời gian chỉ 6.42 mili-giây, khoảng một phần ba; so với co-attention thì nhanh hơn khoảng 3.8 lần. Nên lựa chọn thiết kế ở đây rất rõ: chọn module rẻ nhất, vì không mất gì về độ chính xác.
>
> Em xin nói hai lưu ý để không bị hiểu nhầm. Thứ nhất, bài báo không mô tả đầy đủ giao thức đo thời gian, nên đây là so sánh nội bộ giữa ba module trong cùng điều kiện, không phải latency của một hệ thống production. Thứ hai, và quan trọng hơn: con số 6.42 mili-giây này là chi phí **trong lúc huấn luyện**. Khi inference module này bị bỏ hoàn toàn, nên chi phí thực tế khi truy hồi là **không** — đúng như nhãn đỏ trên slide.
>
> **Nửa dưới là kết quả định tính.** Với cùng một truy vấn, hàng trên là baseline, hàng dưới là IRRA. Trong câu truy vấn, các cụm được tô cam là thuộc tính phân biệt — quần xanh lá, cặp sách đen, giày tennis xanh. Có thể thấy IRRA đưa được nhiều ảnh đúng lên Top-10 hơn, và các ảnh nó chọn đúng thường khớp chính xác ở những cụm được tô cam đó.
>
> Với em, đây là bằng chứng định tính cho đúng cơ chế mà em đã trình bày ở slide MLM: mô hình học được cách liên kết một từ chỉ thuộc tính với đúng vùng ảnh."

### F. Câu chuyển

> "Kết quả thuyết phục, nhưng bài báo vẫn có một hạn chế được chính tác giả thừa nhận và vài câu hỏi còn bỏ ngỏ."

---

# PHẦN THẢO LUẬN VÀ KẾT LUẬN

---

## Slide 22 — IV. Discussion — Limitations and Critical Analysis

**Thời lượng:** ~85 giây

### A. Trên slide có gì

Bốn thẻ đánh số 2×2:

1. `Phrase-level semantics` — *Token masking may distort phrase-level meaning.*
2. `Hard positives` — *ICFG mINP = 7.93: difficult positives remain far down the ranking.*
3. `Generalization` — *No cross-dataset, multilingual, or new-domain evaluation.*
4. `Deployment and ethics` — *No ANN benchmark; privacy, bias, and surveillance risks.*

Dòng chú thích: *(1) is acknowledged by the authors; (2)–(4) are additional critical observations.*

### B. Dẫn vào slide

> "Em xin tách rõ: hạn chế số một là do chính tác giả nêu, còn ba hạn chế sau là đánh giá thêm của em sau khi đọc kỹ bảng số liệu và mã nguồn."

Dòng phân định này quan trọng — nó cho thấy bạn đọc bài báo có phê phán chứ không chép lại phần Conclusion.

### C. Giải thích từng khái niệm

**1. Phrase-level semantics — hạn chế tác giả thừa nhận**

- IRRA chỉ mask **từng token đơn, ngẫu nhiên**. Nên mô hình giỏi ngữ nghĩa ở **cấp từ**, nhưng có thể yếu ở **cấp cụm từ**.
- Ví dụ cụ thể: *"black book bag"* không đơn thuần là tổng của *black* + *book* + *bag*. Nếu che riêng từ *book*, mô hình vẫn đoán được nhờ ngữ cảnh chữ mà không cần thực sự hiểu cụm.
- **Hướng khắc phục:** *span masking* / *phrase masking* — che **cả cụm** cùng lúc, buộc mô hình phải dùng ảnh thay vì dựa vào từ lân cận.

**2. Hard positives — quan sát từ số liệu**

- mINP trên ICFG chỉ **7.93**, trong khi Rank-1 là 63.46. Khoảng cách này rất lớn.
- **Ý nghĩa:** mô hình rất giỏi đưa **một** ảnh đúng lên đầu, nhưng rất yếu trong việc gom **đủ tất cả** ảnh đúng. Những ảnh đúng khó — góc chụp lạ, bị che khuất — vẫn nằm rất xa trong bảng xếp hạng.
- **Hệ quả thực tế:** nếu ứng dụng chỉ cần "tìm ra người này ở đâu đó" thì IRRA rất tốt. Nếu ứng dụng cần "tìm **mọi** lần người này xuất hiện" — ví dụ dựng lại lộ trình qua nhiều camera — thì còn xa mới dùng được.
- Đây chính là lý do bạn đã cài sẵn khái niệm mINP ở slide 18.

**3. Generalization — thiếu bằng chứng**

- Mọi thí nghiệm đều là **within-dataset**: train và test trên cùng một bộ dữ liệu.
- Không có **cross-dataset** (train trên CUHK, test trên ICFG) → chưa biết mô hình chịu được domain shift đến đâu.
- Mọi mô tả đều bằng **tiếng Anh** → chưa biết gì về đa ngôn ngữ. Với ứng dụng ở Việt Nam thì đây là câu hỏi rất thực tế.
- Chưa có đánh giá trên camera mới hoặc điều kiện mới ngoài các bộ có sẵn.

**4. Deployment and ethics**

Hai nhóm riêng biệt, nên tách rõ khi nói:

- **Triển khai:** bài báo tuyên bố inference hiệu quả, nhưng chưa đo chỉ mục ANN, chưa đo footprint bộ nhớ của gallery, chưa đo latency end-to-end. Với học phần cơ sở dữ liệu thì đây đúng là phần còn thiếu.
- **Đạo đức:** person search là công nghệ **lưỡng dụng**. Cần nói ngắn nhưng nghiêm túc:
  - **Riêng tư** — hệ thống cho phép tìm một người cụ thể chỉ bằng lời mô tả, cần cơ chế kiểm soát mục đích sử dụng, phân quyền truy cập và lưu vết truy vấn.
  - **Thiên lệch (bias)** — mô tả bằng ngôn ngữ tự nhiên có thể mang định kiến; bài báo không đánh giá hiệu năng phân tách theo nhóm nhân khẩu học.
  - **Giám sát** — cần khung pháp lý đi kèm, không chỉ là bài toán kỹ thuật.

### D. Slide này giải quyết vấn đề gì

Ba việc:

1. **Chứng minh bạn đọc có phê phán.** Giảng viên thường đánh giá cao phần này hơn phần tóm tắt phương pháp.
2. **Nối các hạn chế với đúng số liệu đã trình bày** (mINP 7.93 ở slide 18–19), chứ không phê phán chung chung.
3. **Mở đường sang slide kết luận** — mỗi hạn chế tương ứng một hướng mở rộng khả thi.

### E. Lời thuyết trình

> "Em xin tách rõ: hạn chế thứ nhất là do chính tác giả nêu trong phần kết luận, còn ba hạn chế sau là đánh giá thêm của em.
>
> **Thứ nhất, ngữ nghĩa cấp cụm từ.** IRRA chỉ mask từng token đơn một cách ngẫu nhiên, nên mô hình thiên về ngữ nghĩa cấp từ. Ví dụ, cụm *black book bag* không đơn thuần là tổng của ba từ riêng lẻ. Nếu chỉ che từ *book*, mô hình vẫn có thể đoán được nhờ hai từ lân cận mà không cần thực sự nhìn ảnh. Tác giả gợi ý phrase-level masking, tức che cả cụm, sẽ phù hợp hơn.
>
> **Thứ hai, hard positive.** Em quay lại con số đã nhắc ở slide chỉ số: mINP trên ICFG chỉ 7.93, trong khi Rank-1 là 63.46. Khoảng cách này rất lớn và nó nói lên một điều cụ thể: mô hình rất giỏi đưa **một** ảnh đúng lên đầu, nhưng rất yếu trong việc gom **đủ tất cả** ảnh đúng. Những ảnh khó — góc chụp lạ, bị che khuất — vẫn nằm rất xa. Nghĩa là nếu ứng dụng chỉ cần tìm ra người này ở đâu đó thì rất tốt; nhưng nếu cần tìm mọi lần người đó xuất hiện, ví dụ dựng lại lộ trình qua nhiều camera, thì còn xa mới dùng được.
>
> **Thứ ba, khả năng tổng quát hóa.** Mọi thí nghiệm đều là within-dataset, train và test trên cùng một bộ. Không có thí nghiệm cross-dataset nên chưa biết mô hình chịu được domain shift đến đâu. Và mọi mô tả đều bằng tiếng Anh — với ứng dụng ở Việt Nam thì đây là câu hỏi rất thực tế.
>
> **Thứ tư, triển khai và đạo đức.** Về triển khai, bài báo nói inference hiệu quả nhưng chưa đo chỉ mục ANN, chưa đo footprint của gallery, chưa đo latency end-to-end — với học phần của chúng ta thì đây đúng là phần còn thiếu. Về đạo đức, đây là công nghệ lưỡng dụng: một hệ thống cho phép tìm ra một người chỉ bằng lời mô tả thì cần cơ chế kiểm soát mục đích sử dụng, phân quyền truy cập và lưu vết truy vấn. Ngoài ra mô tả bằng ngôn ngữ tự nhiên có thể mang định kiến, mà bài báo chưa đánh giá hiệu năng theo nhóm nhân khẩu học."

### F. Câu chuyển

> "Chính các hạn chế này lại mở ra những hướng phát triển rất phù hợp cho đồ án cuối kỳ."

---

## Slide 23 — Three Key Takeaways

**Thời lượng:** ~60 giây

### A. Trên slide có gì

- Ba thẻ đánh số:
  1. `Local relation learning` — *during training; global embeddings at inference*
  2. `IRR + SDM` — *fine-grained interaction and distribution alignment*
  3. `SOTA at CVPR 2023` — *on CUHK-PEDES, ICFG-PEDES, and RSTPReid*
- `POTENTIAL EXTENSIONS`: *Phrase masking • hard-sample mining • multilingual retrieval • vector databases*
- `THANK YOU • Q&A`

### B. Dẫn vào slide

> "Em xin tóm lại ba điều."

### C. Giải thích từng khái niệm

**Ba takeaway — mỗi cái nối về một phần của bài nói:**

1. **Local relation learning during training; global embeddings at inference** — đây là **luận điểm trung tâm**, nối slide 4 (mâu thuẫn) với slide 16 (cách hóa giải).
2. **IRR + SDM** — hai đóng góp kỹ thuật, nối slide 12–14 (cơ chế) với slide 20 (ablation chứng minh cả hai đều cần).
3. **SOTA at CVPR 2023** — bằng chứng, nối slide 19. Nhớ giữ đúng cách phát biểu: *tại thời điểm công bố*.

**Bốn hướng mở rộng — mỗi hướng ứng đúng một hạn chế ở slide 22:**

| Hướng mở rộng | Giải quyết hạn chế nào |
|---|---|
| **Phrase masking** — che cả cụm thay vì token đơn | (1) Ngữ nghĩa cấp cụm từ |
| **Hard-sample mining** — khai thác mẫu khó để tăng mINP | (2) Hard positives |
| **Multilingual retrieval** — truy vấn tiếng Việt | (3) Khả năng tổng quát hóa |
| **Vector databases** — tích hợp FAISS/HNSW, đo latency và recall thật | (4) Triển khai |

Chỉ ra được sự tương ứng một-một này khiến phần kết luận nghe rất chặt chẽ, và nó cũng là gợi ý tự nhiên cho đồ án cuối kỳ.

### D. Slide này giải quyết vấn đề gì

Đóng lại toàn bộ vòng lập luận và để khán giả rời phòng với **đúng một câu** trong đầu. Đừng cố nhắc lại mọi thứ — chỉ cần ba thẻ và câu chốt.

### E. Lời thuyết trình

> "Em xin tóm lại ba điều.
>
> **Một**, và đây là thông điệp cốt lõi: IRRA học quan hệ cục bộ **trong lúc huấn luyện**, nhưng truy hồi bằng embedding toàn cục **khi triển khai**. Đó là cách bài báo hóa giải mâu thuẫn mà em nêu ở đầu bài — giữa nhu cầu chi tiết và nhu cầu tốc độ.
>
> **Hai**, hai đóng góp kỹ thuật: IRR dùng bài toán điền từ bị che để tạo tương tác chi tiết mà không cần nhãn bộ phận; SDM khớp phân phối độ tương đồng với phân phối nhãn để căn chỉnh ở cấp phân phối. Ablation cho thấy cả hai đều cần và bổ sung cho nhau.
>
> **Ba**, mô hình đạt kết quả tốt nhất tại thời điểm công bố trên cả ba benchmark.
>
> Về hướng mở rộng, em để bốn hướng ở đây, và mỗi hướng ứng đúng một hạn chế vừa nêu: phrase masking cho vấn đề cụm từ, hard-sample mining để cải thiện mINP, truy hồi đa ngôn ngữ — chẳng hạn truy vấn tiếng Việt — cho vấn đề tổng quát hóa, và tích hợp vector database để đo latency cùng recall thật, nối trở lại đúng nội dung học phần.
>
> Nếu phải tóm cả bài báo trong một câu, em xin nói: **IRRA đưa chi tiết vào quá trình học, nhưng không đưa chi phí của chi tiết đó vào quá trình truy hồi.**
>
> Em xin cảm ơn thầy cô và các bạn đã lắng nghe. Em sẵn sàng nhận câu hỏi."

---

# APPENDIX — 3 slide dự phòng, không trình bày

## Slide A1 — Appendix A: SDM vs. InfoNCE and CMPM

**Khi nào dùng:** bị hỏi "SDM khác gì các loss contrastive đã có".

| Loss | Tín hiệu chính | Điểm cần nhớ |
|---|---|---|
| **InfoNCE** (loss gốc của CLIP) | Cặp đúng trên đường chéo đối lập với mọi cặp sai trong batch | Giả định **đúng một** positive mỗi hàng; baseline CLIP dùng loss này đã rất mạnh |
| **CMPM** | Cross-modal projection matching — dùng độ dài hình chiếu | Độ dài hình chiếu hoạt động như một scale biến thiên, khó kiểm soát độ nhọn của phân phối; trong cấu hình CLIP chỉ đạt 59.31 trên CUHK |
| **SDM** | KL giữa phân phối similarity và phân phối nhãn theo danh tính | Temperature **cố định** τ=0.02; hỗ trợ **nhiều** positive cùng danh tính; đạt 70.42 trên CUHK |

**Câu trả lời một câu:**
> "SDM biến toàn bộ hàng và cột của ma trận similarity thành phân phối xác suất và buộc nó khớp phân phối nhãn, thay vì chỉ tối ưu một cặp dương trên đường chéo."

---

## Slide A2 — Appendix B: Complete Results

| Dataset | R1 | R5 | R10 | mAP | mINP |
|---|---:|---:|---:|---:|---:|
| CUHK-PEDES | 73.38 | 89.93 | 93.71 | 66.13 | 50.24 |
| ICFG-PEDES | 63.46 | 80.25 | 85.82 | 38.06 | 7.93 |
| RSTPReid | 60.20 | 81.30 | 88.20 | 47.17 | 25.28 |

**Lưu ý về sai khác số liệu trong bản arXiv v1** — chỉ nói nếu bị chất vấn về con số:

- Đoạn văn trang 7 viết CLIP baseline trên CUHK có "Rank-1 và mAP đạt 68.19% và 86.47%". Đây là lỗi diễn đạt: `86.47` là **Rank-5**, còn mAP trong Table 1 là `61.12`.
- Table 1 ghi IRRA Rank-5 trên CUHK là `89.93`, Table 4 ghi `89.83`. README chính thức dùng `89.93` → slide dùng `89.93`.
- ICFG có sai khác làm tròn nhỏ giữa văn bản, Table 2 và README: `80.24/80.25`, `38.05/38.06`, `7.92/7.93`. Tài liệu này dùng số trong Table 2 của bản PDF.
- Phần ablation viết SDM hơn CMPM `2.2` điểm Rank-1 trên RSTPReid, nhưng số trong Table 4 là `57.20 − 55.40 = 1.80`. **Khi trình bày nên dùng số gốc trong bảng**, không lặp lại mức tăng 2.2.

**Cách phát biểu an toàn về SOTA:**
> "State of the art tại thời điểm công bố, so với các baseline được đánh giá trong bài báo."

---

## Slide A3 — Appendix C: Frequently Asked Questions

Xem mục **Ngân hàng câu hỏi** bên dưới — đầy đủ hơn nội dung trên slide.

---

# NGÂN HÀNG CÂU HỎI — chuẩn bị cho Q&A

### Về khái niệm và thiết kế

**1. Tại sao gọi là "implicit" nếu vẫn có cross-attention giữa các local token?**
> Vì hai lý do. Một, mô hình không tạo correspondence bộ phận–cụm từ tường minh và không dùng nhãn body part nào cả. Hai, không có nhánh local matching ở đầu ra khi inference. Quan hệ cục bộ tồn tại như **tín hiệu huấn luyện**, không phải như **thành phần của điểm số truy hồi**.

**2. Vì sao ảnh làm Key/Value còn text làm Query, mà không phải ngược lại?**
> Vì nhiệm vụ cuối cùng là dự đoán **token văn bản** bị che. Mỗi token văn bản cần "hỏi" các vùng ảnh để lấy bằng chứng bổ sung. Làm chiều ngược lại — ảnh hỏi chữ — sẽ không phục vụ trực tiếp cho MLM head.

**3. Bỏ interaction encoder khi inference thì có mất kiến thức không?**
> Không. Gradient từ $\mathcal L_{\mathrm{IRR}}$ đã cập nhật cả image encoder lẫn text encoder theo kiểu end-to-end. Nhánh tương tác đóng vai trò giàn giáo huấn luyện — nó tạo gradient, và gradient đó đã thay đổi trọng số của hai encoder. Tháo giàn giáo thì trọng số đã thay đổi vẫn còn.

**4. Vì sao chọn `[EOS]` làm vector câu chứ không lấy trung bình tất cả token?**
> Vì text encoder của CLIP dùng causal attention: mỗi token chỉ nhìn được phần đứng trước nó. `[EOS]` là token cuối cùng nên là token duy nhất đã "thấy" toàn bộ câu. Đây cũng là thiết kế gốc của CLIP, giữ nguyên để tận dụng trọng số pre-train.

**5. Tổng loss có phải trung bình cộng ba loss không?**
> Không — là **tổng**. Equation (7) và vòng huấn luyện đều cộng trực tiếp; các phép trung bình nằm bên trong từng loss. Code: `total_loss = sum(v for k, v in ret.items() if "loss" in k)` rồi `backward()` một lần.

**6. SDM có xử lý được trường hợp nhiều mô tả cho một ảnh, hoặc nhiều ảnh cho một danh tính không?**
> Có, ở mức danh tính trong phạm vi một mini-batch: mọi cặp có cùng PID được gán $y_{i,j}=1$ rồi chuẩn hóa thành $q$. Mức lợi ích thực tế phụ thuộc cách lấy batch và số positive thực sự cùng xuất hiện trong batch đó.

### Về kết quả và đánh giá

**7. Có thật sự "không tăng chi phí inference" không?**
> So với CLIP dual encoder thì đúng: các module bổ sung đều bị bỏ khi test, số phép mã hóa và số phép tính similarity không đổi. Nhưng bài báo **không** benchmark một vector database end-to-end hay gallery ở quy mô production, nên không nên nói mạnh hơn thế.

**8. Kết quả này còn là SOTA hiện nay không?**
> Không nên khẳng định. Cách nói chính xác là "SOTA trên ba benchmark tại thời điểm CVPR 2023, so với các baseline được đánh giá trong bài báo".

**9. Vì sao mAP thấp hơn Rank-1 nhiều như vậy?**
> Vì chúng đo hai thứ khác nhau. Rank-1 chỉ hỏi có **một** ảnh đúng ở vị trí đầu hay không. mAP tính đến **tất cả** ảnh đúng và vị trí của chúng. Một truy vấn có nhiều ảnh đúng nhưng chỉ đẩy được một ảnh lên đầu sẽ có Rank-1 = 1 nhưng mAP thấp. Đây là hiện tượng bình thường của bài toán truy hồi, không phải dấu hiệu mô hình kém.

**10. Hạn chế quan trọng nhất là gì?**
> Theo tác giả: ngữ nghĩa cấp cụm từ, do chỉ mask token đơn. Theo góc nhìn triển khai của em: thiếu đánh giá cross-domain, đa ngôn ngữ, khả năng mở rộng quy mô, và thiếu đánh giá về riêng tư và thiên lệch.

**11. Vì sao ID loss vẫn được giữ nếu dùng một mình nó làm giảm Rank-1?**
> Vì trong mô hình đầy đủ, khi SDM và IRR đã căn chỉnh tốt hai modality, ID loss bổ sung một lực gom cụm theo danh tính **bên trong** từng modality. Nó là loss bổ trợ, phát huy khi không gian đã có cấu trúc, chứ không tự mình tạo ra cấu trúc đó.

### Về khả năng triển khai và mở rộng

**12. Nếu muốn dùng cho tiếng Việt thì làm thế nào?**
> Có ba hướng. Đơn giản nhất là dịch truy vấn sang tiếng Anh rồi dùng mô hình sẵn có — rẻ nhưng mất mát ngữ nghĩa qua bước dịch. Thứ hai là thay text encoder bằng một encoder đa ngôn ngữ rồi căn chỉnh lại với image encoder. Thứ ba, tốn kém nhất, là thu thập dữ liệu mô tả tiếng Việt và fine-tune. Bài báo không đề cập hướng nào trong số này.

**13. Có thể chạy lại thí nghiệm này không?**
> Được. Repository chính thức có sẵn trong workspace, và bài báo báo cáo chỉ dùng **một** GPU RTX 3090 24 GB với 60 epoch. Lệnh chạy mẫu ở `run_irra.sh` dùng `batch_size 64`.

---

# ĐIỂM CẦN SỬA TRÊN DECK

Trong lúc đối chiếu deck với bài báo và mã nguồn, có bốn điểm nên xử lý trước khi trình bày:

### 1. Slide 15 còn placeholder `PASTE MERMAID FIGURE HERE`

Khung hình lớn bên trái slide ID loss vẫn đang trống. Ba phương án, theo thứ tự khuyến nghị:

- **Phương án A (đơn giản nhất, khuyến nghị):** xóa khung, kéo giãn ba thẻ bên phải ra chiếm cả slide, và phóng to công thức `L_ID` lên giữa. Slide này vốn không cần hình.
- **Phương án B:** vẽ một sơ đồ tĩnh bằng shape của PowerPoint — hai hộp `f_v` và `f_t` cùng chỉ vào một hộp `Shared classifier W`, rồi W chỉ ra `11,003 identity logits`. Khoảng 5 shape, làm trong 3 phút.
- **Phương án C:** vẽ minh họa không gian embedding — các chấm cùng màu (cùng danh tính) tụ lại thành cụm, các cụm tách nhau. Trực quan nhất nhưng tốn thời gian nhất.

### 2. Số thứ tự trang bị nhảy

Số trang hiện tại trên các slide là: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, **15**, **16**, **18**, 19, 20, 21, 22, 23, 24 — thiếu 14 và 17 (dấu vết của hai slide đã xóa). Nên đánh lại liên tục từ 2 đến 23.

### 3. Speaker note của slide 16 hiện đang sai

Note trong file PPTX của slide `Training vs. Inference` đang bắt đầu bằng *"ID loss phân loại cả embedding ảnh và văn bản theo identity…"* — đây là phần sót lại của slide ID loss cũ. Nên thay bằng mục **E** của Slide 16 trong tài liệu này.

### 4. Kích thước từ điển trên slide 9

Slide ghi `BPE vocabulary 49,152`. Con số trong mã nguồn là **49,408** (`utils/options.py: --vocab_size default=49408`). Giải thích: `49,152` là số token sinh từ BPE merge; `49,408` là kích thước từ điển thực tế sau khi thêm các token đặc biệt `<|mask|>`, `<|startoftext|>`, `<|endoftext|>` (xem `utils/simple_tokenizer.py`).

Đây là chi tiết nhỏ, nhưng nếu giảng viên có đọc code thì sẽ thấy. Đề xuất: sửa thành `49,408` hoặc ghi `~49k`.

---

# PHƯƠNG ÁN RÚT GỌN THEO THỜI LƯỢNG

### Nếu được 20–25 phút — trình bày đủ 23 slide

Theo đúng thời lượng trong bảng ở đầu tài liệu. Dành nhiều thời gian nhất cho slide 8, 12, 13, 14 và 16.

### Nếu chỉ còn 15 phút

- **Bỏ:** slide 10 và 11 (chi tiết bên trong Transformer block). Thay bằng một câu ở slide 9: *"Cả hai encoder đều dùng Transformer 12 block với residual pre-LayerNorm; điểm khác biệt duy nhất là text encoder dùng causal mask, nên `[EOS]` tổng hợp được toàn câu."*
- **Rút gọn:** slide 17 và 18 gộp lại nói trong 60 giây.
- **Giữ nguyên:** 4, 5, 7, 8, 12, 13, 14, 16, 19, 20, 22, 23 — đây là xương sống.

### Nếu chỉ còn 10 phút

- Giữ: 1, 2, 4, 5, 7, 8, 12, 16, 19, 20, 23.
- Slide 14 (SDM): chỉ nói một câu — *"SDM khớp cả hình dạng phân phối độ tương đồng với phân phối nhãn, thay vì chỉ nâng điểm một cặp đúng."*
- Bỏ slide 22, chuyển phần hạn chế thành một câu ở slide 23.

### Ba slide tuyệt đối không được bỏ

| Slide | Lý do |
|---|---|
| **4** — Why difficult | Không có nó thì phương pháp nghe như kỹ thuật rời rạc, không ai hiểu vì sao cần |
| **12** — IRR through MLM | Đây là ý tưởng của bài báo |
| **16** — Train vs Inference | Đây là luận điểm của bài báo, và là chỗ nối với học phần |

---

# TÀI LIỆU THAM KHẢO

1. D. Jiang and M. Ye, "Cross-Modal Implicit Relation Reasoning and Aligning for Text-to-Image Person Retrieval," *Proceedings of CVPR*, pp. 2787–2797, 2023. Bản trong workspace: [`2303.12501v1.pdf`](2303.12501v1.pdf)
2. Trang chính thức CVF: <https://openaccess.thecvf.com/content/CVPR2023/html/Jiang_Cross-Modal_Implicit_Relation_Reasoning_and_Aligning_for_Text-to-Image_Person_Retrieval_CVPR_2023_paper.html>
3. Mã nguồn chính thức: <https://github.com/anosorae/IRRA> — bản trong workspace: [`../IRRA/`](../IRRA/)
4. A. Radford et al., "Learning Transferable Visual Models From Natural Language Supervision," 2021. Giới thiệu CLIP: <https://openai.com/index/clip/>
5. J. Devlin et al., "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," NAACL 2019 — nguồn của quy tắc masking 15% và 80/10/10.
