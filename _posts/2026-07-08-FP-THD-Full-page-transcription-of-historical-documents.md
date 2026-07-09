---
title: "FP-THD: Full page transcription of historical documents"
subtitle:  
layout: post
image: /images/posts/2026-07-08-workflow.jpg
categories: [Paper overview]
---

Historical document transcription remains challenging due to complex layouts, diverse writing styles, and the presence of obsolete characters and abbreviations. Our recently published paper, "FP-THD: Full page transcription of historical documents", presents an end-to-end pipeline designed for automatic full-page transcription. 

The proposed framework combines four main components: layout analysis, text line extraction, OCR recognition, and result representation. A deep learning-based layout analysis module identifies text regions and baselines, allowing the extraction and normalization of individual text lines before recognition. The OCR stage relies on a Masked Autoencoder with Vision Transformer (MAE-ViT) architecture enhanced with span masking and CTC decoding to recognize handwritten and printed historical texts without requiring external language models or post-processing.

![Fig. 1. Workflow of our proposed pipeline for full page transcription of historical documents (FP-THD)]({{ site.baseurl }}/images/posts/2026-07-08-workflow.jpg){: .center-image width="100%"}
<h4><center><b>Fig. 1. Workflow of our proposed pipeline for full page transcription of historical documents (FP-THD)</b></center></h4>

The system was evaluated on multiple historical datasets, including handwritten manuscripts (Rodrigo and Bentham) and a newly created printed-text dataset (Molino) containing medieval Latin documents with abbreviations. The proposed approach achieved competitive performance for handwritten text recognition and demonstrated high accuracy for full-page transcription. On the Molino dataset, FP-THD reached 1.14% Character Error Rate (CER) and 4.85% Word Error Rate (WER), outperforming existing OCR solutions such as ABBYY, Pero-OCR, and TrOCR.

By preserving historical spelling, diacritics, abbreviations, and special characters, FP-THD provides a reliable solution for digital humanities applications, enabling accurate analysis and further processing of historical archives.

---
[FP-THD: Full page transcription of historical documents.](https://doi.org/10.1016/j.patcog.2026.114351)  H. NEJI, J. NOGUERAS-ISO, J. LACASTA, M.Á. LATRE, F.J. GARCÍA-MARCO. Pattern Recognition, vol. 180(part D), 114351, 2026.

---
