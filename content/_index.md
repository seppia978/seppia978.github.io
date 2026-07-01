---
# Leave the homepage title empty to use the site title
title: ""
date: 2022-10-24
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    id: about
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: /uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: markdown
    id: research
    content:
      title: Research Focus
      subtitle: ''
      text: |-
        <p class="research-lede">
          I study how to control, understand, and audit AI systems before and after deployment, with a focus on models that must remain reliable under fine-tuning, misuse, and distribution shift.
        </p>

        <div class="research-focus-grid">
          <div class="research-focus-card">
            <h3>AI Control Across Deployment</h3>
            <p>Methods and evaluations for keeping language, vision-language, and generative models aligned before release and robust after fine-tuning, adaptation, or policy shifts.</p>
          </div>
          <div class="research-focus-card">
            <h3>The Mechanics of Model Change</h3>
            <p>Interpreting how fine-tuning changes models, from multilingual LLM safety to gravitational interpretations of fine-tuning reversion and future mechanistic studies.</p>
          </div>
          <div class="research-focus-card">
            <h3>Evidence, Forgetting & Forensics</h3>
            <p>Tools to explain decisions, remove learned information, and assess synthetic media, connecting XAI, unlearning, and deepfake robustness under one reliability lens.</p>
          </div>
        </div>

        <div class="research-quick-links">
          <a href="#papers">Selected publications</a>
          <a href="#talks">Talks and lectures</a>
          <a href="/uploads/resume.pdf">Download CV</a>
          <a href="mailto:s.poppi94@gmail.com">Start a conversation</a>
        </div>
    design:
      columns: '1'
      css_class: research-focus-section
  - block: markdown
    id: news
    content:
      title: Latest News
      subtitle: ''
      text: |-
        <p class="latest-news-meta">
          Selected venues: ECCV x2 · NAACL Findings x1 · ICPR x1 · ICIAP x2 · IEEE Intelligent Systems x1 · CVPRW x1
        </p>

        <ul class="latest-news-list">
          <li><time>Jun'26</time><span><a href="/publication/2606-arxiv-finetuning_reversion/">A Gravitational Interpretation of Fine-Tuning Reversion</a> is online on arXiv.</span></li>
          <li><time>Jun'26</time><span><a href="/publication/2606-arxiv-cot_knows_better/">When the Chain of Thought Knows Better</a> is online on arXiv.</span></li>
          <li><time>Mar'26</time><span><a href="/publication/2603-arxiv-activation_watermarking/">Robust Safety Monitoring of Language Models via Activation Watermarking</a> is online on arXiv.</span></li>
          <li><time>Dec'25</time><span><a href="/publication/2512-arxiv-authentic_multimedia_detection/">Robust and Calibrated Detection of Authentic Multimedia Content</a> is online on arXiv.</span></li>
          <li><time>Nov'25</time><span><a href="/publication/2511-eccv-spqr/">SPQR</a> accepted at ECCV 2026.</span></li>
          <li><time>Nov'25</time><span>I gave a lecture on safety for text-to-image diffusion models at MBZUAI.</span></li>
          <li><time>Jun'25</time><span>I joined MBZUAI as a Postdoctoral Associate in the SPOT Lab.</span></li>
          <li><time>May'25</time><span>I completed my PhD and gave a lecture on responsible generative AI at Scuola Normale Superiore.</span></li>
        </ul>
    design:
      columns: '1'
      css_class: latest-news-section
  - block: collection
    id: papers
    content:
      title: Selected Publications
      text: Recent work at the intersection of AI safety, robustness, and trustworthy generative models.
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    content:
      title: More Publications
      text: Additional papers and earlier work.
      count: 4
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Talks & Lectures
      filters:
        folders:
          - event
    design:
      view: article-grid
      columns: 1
  - block: markdown
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: |-
        I am always happy to discuss AI safety, robust evaluation, trustworthy multimodal systems, and collaborations around model behavior under adaptation.

        <div class="research-quick-links">
          <a href="mailto:s.poppi94@gmail.com">Email me</a>
          <a href="https://scholar.google.com/citations?user=EBLQPgcAAAAJ&hl=en">Google Scholar</a>
          <a href="https://github.com/seppia978">GitHub</a>
          <a href="https://www.linkedin.com/samuele-poppi">LinkedIn</a>
        </div>
    design:
      columns: '1'
      css_class: research-focus-section
---
