---
title: 'Unveiling the Impact of Image Transformations on Deepfake Detection: An Experimental Analysis'

# Authors
# If you created a profile for a user (e.g. the default `admin` user), write the username (folder name) here
# and it will be replaced with their full name and linked to their profile.
authors:
  - Federico Cocchi
  - Lorenzo Baraldi
  - admin
  - Marcella Cornia
  - Lorenzo Baraldi
  - Rita Cucchiara

# Author notes (optional)
author_notes:
  - 'Equal contribution'
  - 'Equal contribution'

date: '2023-09-05T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'

# Publication type.
# Accepts a single type but formatted as a YAML list (for Hugo requirements).
# Enter a publication type from the CSL standard.
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *22nd International Conference on Image Analysis and Processing 2023*
publication_short: In *ICIAP*
abstract: With the recent explosion of interest in visual Generative AI, the field of deepfake detection has gained a lot of attention. In fact, deepfake detection might be the only measure to counter the potential proliferation of generated media in support of fake news and its consequences. While many of the available works limit the detection to a pure and direct classification of fake versus real, this does not translate well to a real-world scenario. Indeed, malevolent users can easily apply post-processing techniques to generated content, changing the underlying distribution of fake data. In this work, we provide an in-depth analysis of the robustness of a deepfake detection pipeline, considering different image augmentations, transformations, and other pre-processing steps. These transformations are only applied in the evaluation phase, thus simulating a practical situation in which the detector is not trained on all the possible augmentations that can be used by the attacker. In particular, we analyze the performance of a k-NN and a linear probe detector on the COCOFake dataset, using image features extracted from pre-trained models, like CLIP and DINO.  Our results demonstrate that while the CLIP visual backbone outperforms DINO in deepfake detection with no augmentation, its performance varies significantly in presence of any transformation, favoring the robustness of DINO.

# Summary. An optional shortened abstract.
# summary: Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis posuere tellus ac convallis placerat. Proin tincidunt magna sed ex sollicitudin condimentum.

tags:
  - DeepFakes
  - Image Transformations
  - CLIP
  - DINO

# Display this page in the Featured widget?
featured: false

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://iris.unimore.it/bitstream/11380/1309209/6/2023-iciap-deepfake.pdf'
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
