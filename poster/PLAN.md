# Plan: Poster A0 cho AC5211 (LoRA + SDM trên RSTPReid)

Nội dung poster là bản rút gọn của báo cáo 6 trang `../final-report/main.pdf`, viết bằng tiếng Anh.

## 1. Quyết định

| # | Quyết định | Chốt | Trạng thái |
|---|---|---|---|
| 1 | Khổ và hướng giấy | **A0 dọc** (841 × 1189 mm), 2 cột. Không có template của môn nên dùng `tikzposter` cơ bản | ✅ |
| 2 | Phong cách và màu | **Tối giản kiểu bài báo IEEE**: theme `Simple`, nền trắng, chữ đen, viền khối xám mảnh. Chỉ thêm **1 màu nhấn** là xanh IEEE `#00629B` cho tiêu đề khối và câu kết luận. Trong biểu đồ chỉ giữ 3 màu loss của Fig. 2 | ✅ |
| 3 | Tên tác giả | Viết không dấu: **Do Thanh Tung** (để compile được bằng pdfLaTeX) | ✅ |
| 4 | QR code | QR 10 cm ở góc phải header, trỏ tới `github.com/thanhtungdo2211/master-thesis` (repo đã public, kiểm tra ngày 2026-11-09) | ✅ |

## 2. Quy chuẩn poster A0

- Khoảng **550 từ, tối đa 800**.
- Tỉ lệ: khoảng 40% chữ, 60% hình/bảng, 20–30% khoảng trắng.
- Cỡ chữ:

  | Thành phần | Cỡ chữ |
  |---|---|
  | Tiêu đề | 72–120 pt |
  | Tiêu đề khối | 48–60 pt |
  | Nội dung | 28–36 pt, không nhỏ hơn 24 pt |
  | References | 18–24 pt |

- Tối đa 2–3 công thức. Font sans-serif.
- Kiểm tra cỡ chữ: in poster ra 1 tờ A4. Nếu đọc được phần nội dung thì khi in A0 sẽ đạt.

## 3. Bố cục (theo mặc định A0 dọc, 2 cột)

```
+--------------------------------------------------------------+
| TITLE: LoRA Meets SDM ...      Do Thanh Tung · 20252432M  [QR]|
+------------------------------+-------------------------------+
| 1. Motivation & Questions    | 4. Q1: LoRA vs full FT        |
|  - Q1, Q2                    |  bar chart R@1 + params       |
|  - box "Existing vs Ours"    |  58.85 / 57.18 vs 57.20       |
+------------------------------+  0.49M vs 149.6M (×304)       |
| 2. Method                    +-------------------------------+
|  Fig.1 pipeline (big)        | 5. Q2: where does SDM help?   |
|  LoRA r=4, 96 modules        |  Fig.2 curves (big)           |
+------------------------------+  MPCE ≈ InfoNCE (0.18)        |
| 3. Key insight (theory)      |  SDM − MPCE = +3.15           |
|  1.52% rows có 2nd positive  +-------------------------------+
|  SDM ≈ λ(1−p) − H(p)         | 6. Takeaways + FL outlook     |
|  plot: gradient weight       |  3 bullets + câu kết luận lớn |
|  (1−p) vs λp(1−p)            | References (4) · contact      |
+------------------------------+-------------------------------+
```

**Thông điệp chính (in to):** *"SDM's gain comes from the KL direction, not from multiple positives."*

### Nội dung từng khối

| Khối | Số từ | Nguồn từ báo cáo | Hình/bảng |
|---|---|---|---|
| 1. Motivation & Questions | 60–80 | Sec. I, Table I | Box 2 cột "Existing (IRRA, CLIP, LoRA)" và "Ours" |
| 2. Method | 80–100 | Sec. IV-A | Fig. 1 pipeline, phóng to |
| 3. Key insight | 80–100 | Sec. IV-B, Eq. (6)–(8) | **Hình mới:** trọng số gradient theo p |
| 4. Q1 results | 60–80 | Sec. V-B, Table II | **Hình mới:** biểu đồ cột R@1 |
| 5. Q2 results | 80–100 | Sec. V-C, Table III | Fig. 2 (R@1 và mAP theo epoch), phóng to |
| 6. Takeaways + FL | 60–80 | Sec. V-D, VII | 3 bullet, references, contact |

## 4. Hình mới (chỉ có trên poster)

1. **Biểu đồ cột R@1:** IRRA full FT InfoNCE 54.05, IRRA full FT SDM 57.20, IRRA full 60.20, LoRA InfoNCE, LoRA MPCE, LoRA SDM. Số tham số train ghi trên mỗi cột. Số của IRRA lấy từ paper; số của LoRA lấy từ `generated/numbers.tex`.
2. **Đồ thị trọng số gradient** trên cặp đúng, theo p ∈ (0, 1):
   - InfoNCE: (1 − p)
   - SDM: λ·p(1 − p), với λ = 18.42

   Đây là hình giải tích, không phải dữ liệu từ run. Nó minh họa việc SDM bỏ qua các cặp quá khó (p → 0), còn InfoNCE dồn lực vào chính các cặp đó.

## 5. Kỹ thuật

- LaTeX `tikzposter` (template `latex-document` skill: `assets/templates/poster.tex`), dùng `\usetheme{Simple}` và màu tối giản như mục 1, compile bằng pdfLaTeX.
- Thư mục: `AC5211/poster/` gồm:
  - `poster.tex`
  - `figures/`
  - dùng chung `../final-report/generated/numbers.tex` và `curve_*.csv`, để số liệu poster luôn khớp với báo cáo
- Màu các đường loss giữ đúng như Fig. 2 của báo cáo: SDM `#2A78D6`, MPCE `#EB6834`, InfoNCE `#1BAF7A`.
- Quy tắc: không gõ tay số liệu từ run; số của IRRA phải trích dẫn nguồn.

## 6. Các bước

- [x] 0. Chốt khổ giấy, màu, tên, QR (mục 1)
- [x] 1. Dựng khung `tikzposter` theo khổ, màu và bố cục đã chốt
- [x] 2. Viết nội dung rút gọn từ báo cáo
- [x] 3. Vẽ 2 hình mới (pgfplots) và phóng to Fig. 1, Fig. 2
- [x] 4. Compile, xuất PNG preview (`preview/poster-1.png`); đã kiểm tra cỡ chữ, tràn khung. **Còn:** in thử 1 trang A4 và quét thử QR bằng điện thoại
- [ ] 5. Duyệt và chỉnh sửa theo góp ý
- [ ] 6. Xuất PDF vector và in A0 (giấy couché hoặc decal, tỉ lệ 100%)
