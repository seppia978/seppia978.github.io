---
title: ''
date: 2022-10-24
type: landing

design:
  spacing: '4.5rem'

sections:
  - block: markdown
    id: about
    content:
      title: ''
      subtitle: ''
      text: |-
        <div class="editorial-hero">
          <div class="editorial-hero-main">
            <p class="eyebrow">Postdoctoral Associate · AI Safety</p>
            <h1>Samuele Poppi</h1>
            <p class="hero-statement">I study how AI systems change after deployment, adaptation, and misuse.</p>
            <p class="hero-copy">My work connects safety control, mechanistic understanding, and trustworthy evidence for language, vision-language, and generative models after they leave the lab.</p>
            <div class="hero-chips" aria-label="Research focus areas">
              <a href="/research/#threads">AI Control</a>
              <a href="/research/#threads">Model Change</a>
              <a href="/research/#threads">Forensics</a>
            </div>
            <div class="hero-actions">
              <a href="/uploads/resume.pdf">CV</a>
              <a href="https://scholar.google.com/citations?user=EBLQPgcAAAAJ&amp;hl=en">Scholar</a>
              <a href="https://github.com/seppia978">GitHub</a>
              <a href="mailto:s.poppi94@gmail.com">Email</a>
            </div>
          </div>
          <aside class="current-panel" aria-label="Current status">
            <img class="current-avatar" src="/author/samuele-poppi/avatar.jpg" alt="Samuele Poppi">
            <div>
              <p class="panel-label">Currently</p>
              <p class="panel-title">Postdoc, MBZUAI SPOT Lab</p>
              <p class="panel-copy">Working on model behavior under fine-tuning, safety alignment under adaptation, and robust evidence for trustworthy AI.</p>
            </div>
            <div class="panel-highlight">
              <span>Latest</span>
              <a href="/publication/2511-eccv-spqr/">SPQR accepted at ECCV 2026</a>
            </div>
          </aside>
        </div>
    design:
      columns: '1'
      css_class: editorial-hero-section
  - block: markdown
    id: news
    content:
      title: Latest News
      subtitle: ''
      text: |-
        <div class="news-board">
          <p class="latest-news-meta">Selected venues: ECCV x2 · ICPR x2 · NAACL Findings x1 · ICIAP x2 · IEEE Intelligent Systems x1 · CVPRW x1</p>
          <ul class="latest-news-list">
            <li><time>Jun 2026</time><span><a href="/publication/2511-eccv-spqr/">SPQR</a> accepted at ECCV 2026.</span></li>
            <li><time>Jun 2026</time><span><a href="/publication/2606-arxiv-finetuning_reversion/">A Gravitational Interpretation of Fine-Tuning Reversion</a> is online on arXiv.</span></li>
            <li><time>Jun 2026</time><span><a href="/publication/2606-arxiv-cot_knows_better/">When the Chain of Thought Knows Better</a> is online on arXiv.</span></li>
            <li><time>Mar 2026</time><span><a href="/publication/2603-arxiv-activation_watermarking/">Robust Safety Monitoring of Language Models via Activation Watermarking</a> is online on arXiv.</span></li>
            <li><time>Dec 2025</time><span><a href="/publication/2512-arxiv-authentic_multimedia_detection/">Robust and Calibrated Detection of Authentic Multimedia Content</a> is online on arXiv.</span></li>
            <li><time>Nov 2025</time><span>I gave a lecture on safety for text-to-image diffusion models at MBZUAI.</span></li>
            <li><time>Jun 2025</time><span>I joined MBZUAI as a Postdoctoral Associate in the SPOT Lab.</span></li>
            <li><time>May 2025</time><span>I completed my PhD and gave a lecture on responsible generative AI at Scuola Normale Superiore.</span></li>
          </ul>
        </div>
    design:
      columns: '1'
      css_class: latest-news-section
  - block: markdown
    id: research-preview
    content:
      title: Research Threads
      subtitle: ''
      text: |-
        <p class="research-lede">Three connected views of the same question: how do we keep AI systems reliable when deployment changes the model, the context, and the evidence we can trust?</p>
        <div class="research-focus-grid">
          <a class="research-focus-card" href="/research/#threads">
            <span>01</span>
            <h3>AI Control Across Deployment</h3>
            <p>Control mechanisms and evaluations that survive fine-tuning, adaptation, and downstream customization.</p>
          </a>
          <a class="research-focus-card" href="/research/#threads">
            <span>02</span>
            <h3>The Mechanics of Model Change</h3>
            <p>Mechanistic and geometric views of how models shift under multilingual attacks and post-alignment updates.</p>
          </a>
          <a class="research-focus-card" href="/research/#threads">
            <span>03</span>
            <h3>Evidence, Forgetting &amp; Forensics</h3>
            <p>XAI, unlearning, watermarking, and multimedia forensics as tools for evidence under uncertainty.</p>
          </a>
        </div>
    design:
      columns: '1'
      css_class: research-focus-section
  - block: collection
    id: papers
    content:
      title: Featured Work
      text: Recent work at the intersection of AI safety, robustness, and trustworthy generative models.
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      columns: 2
  - block: collection
    id: more-papers
    content:
      title: More Publications
      text: Additional papers and earlier work.
      count: 5
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
      columns: 2
  - block: markdown
    id: contact
    content:
      title: Contact
      subtitle: ''
      text: |-
        <div class="contact-panel">
          <p>I am always happy to discuss AI safety, robust evaluation, trustworthy multimodal systems, and collaborations around model behavior under adaptation.</p>
          <div class="research-quick-links">
            <a href="mailto:s.poppi94@gmail.com">Email me</a>
            <a href="https://scholar.google.com/citations?user=EBLQPgcAAAAJ&amp;hl=en">Google Scholar</a>
            <a href="https://github.com/seppia978">GitHub</a>
            <a href="https://www.linkedin.com/samuele-poppi">LinkedIn</a>
          </div>
        </div>
    design:
      columns: '1'
      css_class: contact-section
---
