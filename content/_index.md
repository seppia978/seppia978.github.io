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
          I study how AI systems fail, adapt, and stay safe after deployment, with a focus on LLMs, multimodal models, and generative systems that must remain reliable under fine-tuning, misuse, and distribution shift.
        </p>

        <div class="research-focus-grid">
          <div class="research-focus-card">
            <h3>Safety after adaptation</h3>
            <p>Benchmarks and stress tests for safety alignment when models are fine-tuned, personalized, or moved into new domains.</p>
          </div>
          <div class="research-focus-card">
            <h3>Multilingual LLM safety</h3>
            <p>Understanding how safety behavior transfers across languages, and why fine-tuning attacks can break alignment globally.</p>
          </div>
          <div class="research-focus-card">
            <h3>Trustworthy multimodal AI</h3>
            <p>Methods for safer vision-language and text-to-image systems, from concept removal to robust evaluation protocols.</p>
          </div>
          <div class="research-focus-card">
            <h3>Unlearning and provenance</h3>
            <p>Practical tools for removing information, resisting watermark forgery, and making generated media more accountable.</p>
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
  - block: collection
    id: news
    content:
      title: Updates
      subtitle: ''
      text: ''
      # Page type to display. E.g. post, talk, publication...
      page_type: post
      # Choose how many pages you would like to display (0 = all pages)
      count: 5
      # Filter on criteria
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      # Choose how many pages you would like to offset by
      offset: 0
      # Page order: descending (desc) or ascending (asc) date.
      order: desc
    design:
      # Choose a layout view
      view: date-title-summary
      # Reduce spacing
      spacing:
        padding: [0, 0, 0, 0]
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
