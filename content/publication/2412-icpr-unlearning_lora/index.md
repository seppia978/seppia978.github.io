---
title: 'Unlearning Vision Transformers without Retaining Data via Low-Rank Decompositions'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - admin
  - Sara Sarto
  - Marcella Cornia
  - Lorenzo Baraldi'
  - Rita Cucchiara

# Author notes (optional)
author_notes:

date: '2024-12-01T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *International Conference on Pattern Recognition*
publication_short: In *ICPR*
abstract: The implementation of data protection regulations such as the GDPR and the California Consumer Privacy Act has sparked a growing interest in removing sensitive information from pre-trained models without requiring retraining from scratch, all while maintaining predictive performance on remaining data. Recent studies on machine unlearning for deep neural networks have resulted in different attempts that put constraints on the training procedure and which are limited to small-scale architectures and with poor adaptability to real-world requirements. In this paper, we develop an approach to delete information on a class from a pre-trained model, by injecting a trainable low-rank decomposition into the network parameters, and without requiring access to the original training set. Our approach greatly reduces the number of parameters to train as well as time and memory requirements. This allows a painless application to real-life settings where the entire training set is unavailable, and compliance with the requirement of time-bound deletion. We conduct experiments on various Vision Transformer architectures for class forgetting. Extensive empirical analyses demonstrate that our proposed method is efficient, safe to apply, and effective in removing learned information while maintaining accuracy.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - Unlearning
  - Trustworthy AI
  - Transformers

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://iris.unimore.it/bitstream/11380/1350486/2/2024_ICPR_Unlearning.pdf'
# url_code: 'https://github.com/aimagelab/safe-clip'
# url_dataset: 'https://huggingface.co/datasets/aimagelab/ViSU-Text'
# url_poster: ''
# url_project: 'https://aimagelab.github.io/safe-clip/'
# url_slides: ''
# url_source: 'https://github.com/HugoBlox/hugo-blox-builder'
# url_video: 'https://youtube.com'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: '' #Image credit: [**Unsplash**](https://unsplash.com/photos/pLCdAaMFLTE)'
  focal_point: ''
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - ELIAS

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---

<!-- {{% callout note %}}
Click the _Cite_ button above to demo the feature to enable visitors to import publication metadata into their reference management software.
{{% /callout %}}

{{% callout note %}}
Create your slides in Markdown - click the _Slides_ button to check out the example.
{{% /callout %}} -->

<!-- Add the publication's **full text** or **supplementary notes** here. You can use rich formatting such as including [code, math, and images](https://docs.hugoblox.com/content/writing-markdown-latex/). -->
