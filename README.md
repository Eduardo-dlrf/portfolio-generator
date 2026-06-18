# Portfolio Feed Generator

A custom, Docker-powered GitHub Action to dynamically generate a professional Atom syndicated feed from a clean, human-readable YAML file. 
Instead of manually maintaining complex XML/Atom tags, this action automates the processing of career milestones, technical certifications, and project documents.

## Usage

### 1. Turn on GitHub Pages
In your repository, go to **Settings > Pages** and select the `main` branch as the source. This provides a base URL for hosting your public assets and portfolio feed. Note this URL for the configuration step below.

### 2. Create the Portfolio YAML File
Create a file named `portfolio.yaml` in the root of your repository using the following structured format to log your profile data and technical achievements:

```yaml
title: "Eduardo's Engineering & Automation Portfolio"
subtitle: "Showcasing automotive optimization, continuous learning, and software automation"
author: "Eduardo"
description: "A digital log of my professional milestones, engineering achievements, and technical certifications."
link: <Your GitHub Pages URL e.g., [https://Eduardo-dlrf.github.io/Portfolio/](https://Eduardo-dlrf.github.io/Portfolio/)>
image: </images/profile.jpg (Relative path to your profile picture)>
language: "en-us"
category: "Engineering"

item:
  - title: <Project or Milestone Title e.g., Bachelor Thesis at BMW Group>
    description: <Detailed technical summary of your achievement and impact>
    published: "<ISO-8601 Date Format e.g., 2026-01-15T09:00:00Z (Must be inside quotes)>"
    file: <Path or link to documentation e.g., /documents/thesis_report.pdf or GitHub URL>
    type: <MIME type e.g., application/pdf or text/html>
    preview_img: </images/screenshot.png (Optional: Relative path to a project showcase image)>

  # Repeat the block above for each certification, thesis, or automation tool you want to display
```
3. Sample Workflow Configuration
To automate the production-ready build every time you push a change to your data, create a workflow file at .github/workflows/main.yml:
```
name: Generate Feed
on: [push]

jobs:
  generate-feed:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3
        
      - name: Run Feed Generator
        uses: eduardo-dlrf/portfolio-generator@main
```
