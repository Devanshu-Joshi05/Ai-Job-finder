import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "TalentAI – Smart AI Job Finder & Career Growth Platform")
            self.drawRightString(612 - 54, 750, "Project Summary Report")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 612 - 54, 742)

        # Footer
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 45, 612 - 54, 45)
        self.drawString(54, 32, "Confidential | Prepared for Academic Evaluation")
        self.drawRightString(612 - 54, 32, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf():
    pdf_filename = "TalentAI_Project_Report.pdf"
    doc = SimpleDocTemplate(
        pdf_filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor("#1E1B4B")      # Deep Navy
    ACCENT = colors.HexColor("#4F46E5")       # Royal Indigo
    EMERALD = colors.HexColor("#059669")      # Green
    ROSE = colors.HexColor("#E11D48")         # Red
    TEXT = colors.HexColor("#0F172A")         # Dark Charcoal
    MUTED = colors.HexColor("#475569")        # Slate Muted
    LIGHT_BG = colors.HexColor("#F8FAFC")     # Soft Gray

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=PRIMARY,
        spaceAfter=6
    )

    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=ACCENT,
        spaceAfter=14
    )

    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=PRIMARY,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    h2_style = ParagraphStyle(
        'SectionH2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=ACCENT,
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=TEXT,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'BulletText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=TEXT,
        leftIndent=14,
        spaceAfter=4
    )

    callout_style = ParagraphStyle(
        'CalloutText',
        parent=styles['Normal'],
        fontName='Helvetica-Oblique',
        fontSize=9.5,
        leading=14,
        textColor=PRIMARY
    )

    story = []

    # ================= COVER BANNER =================
    banner_data = [
        [
            Paragraph("<b>ACADEMIC MAJOR PROJECT REPORT</b>", ParagraphStyle('B1', fontName='Helvetica-Bold', fontSize=10, textColor=EMERALD)),
        ],
        [
            Paragraph("TalentAI: Smart AI Job Finder & Career Growth Platform", title_style),
        ],
        [
            Paragraph("An Intelligent Cross-Platform Mobile & Web Ecosystem Featuring Scam Job Detection, ATS Resume Optimization, and Real-Time Application Tracking", subtitle_style),
        ]
    ]
    banner_table = Table(banner_data, colWidths=[504])
    banner_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), LIGHT_BG),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor("#CBD5E1")),
        ('LEFTPADDING', (0,0), (-1,-1), 16),
        ('RIGHTPADDING', (0,0), (-1,-1), 16),
        ('TOPPADDING', (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('ROUNDEDCORNERS', [6, 6, 6, 6])
    ]))
    story.append(banner_table)
    story.append(Spacer(1, 14))

    # Meta Info Table
    meta_data = [
        [
            Paragraph("<b>Project Domain:</b> Artificial Intelligence & Full-Stack Web/Mobile", body_style),
            Paragraph("<b>Deployment:</b> Live Web (PWA) & Android Native APK", body_style)
        ],
        [
            Paragraph("<b>Target Audience:</b> Engineering Students & Fresh Graduates", body_style),
            Paragraph("<b>Live URL:</b> <font color='#4F46E5'><u>https://talentai-rohan.surge.sh</u></font>", body_style)
        ]
    ]
    meta_table = Table(meta_data, colWidths=[252, 252])
    meta_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#EEF2F6")),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LINEBELOW', (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
    ]))
    story.append(meta_table)
    story.append(Spacer(1, 16))

    # ================= 1. ABSTRACT =================
    story.append(Paragraph("1. Executive Summary & Abstract", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    abstract_text = (
        "<b>TalentAI</b> is an end-to-end career intelligence solution engineered to address critical inefficiencies in college placements "
        "and graduate hiring. Freshers face two monumental hurdles: falling prey to fraudulent job postings that charge fake fees, and having "
        "their resumes automatically filtered out by Applicant Tracking Systems (ATS). TalentAI combines an automated rule-based scam classifier, "
        "an instant ATS resume keyword optimizer with real-time PDF generation, a verified repository of 102+ active corporate opportunities "
        "(Google, Microsoft, Swiggy, Zomato, TCS), and an interactive Kanban application tracker into a single ultra-fast, mobile-friendly application."
    )
    story.append(Paragraph(abstract_text, body_style))
    story.append(Spacer(1, 10))

    # ================= 2. PROBLEM STATEMENT =================
    story.append(Paragraph("2. Problem Statement & Motivation", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    
    problems = [
        ("Proliferation of Job Scams:", "Fake recruiters exploit desperate job seekers by requiring 'security deposits', training fees, or redirecting to anonymous Telegram groups."),
        ("High ATS Rejection Rates (75%+):", "Most student resumes lack the exact industry keywords or clean formatting required by modern automated hiring engines."),
        ("Disorganized Application Pipelines:", "Students apply across 5+ disparate platforms (LinkedIn, Naukri, Indeed, Company portals) without an integrated milestone tracker.")
    ]
    for p_t, p_d in problems:
        story.append(Paragraph(f"• <b>{p_t}</b> {p_d}", bullet_style))
    story.append(Spacer(1, 10))

    # ================= 3. CORE ARCHITECTURE =================
    story.append(Paragraph("3. Technical Architecture & System Modules", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))

    module_data = [
        [Paragraph("<b>System Module</b>", h2_style), Paragraph("<b>Engineering Implementation</b>", h2_style), Paragraph("<b>Key Output</b>", h2_style)],
        [
            Paragraph("<b>1. Verified Feed Aggregator</b>", body_style),
            Paragraph("Ingests structured corporate catalog (102+ openings) with fallback to RapidAPI JSearch live web feeds.", body_style),
            Paragraph("Zero-latency instant rendering of top Indian tech jobs.", body_style)
        ],
        [
            Paragraph("<b>2. AI Scam Shield</b>", body_style),
            Paragraph("Multi-rule heuristic analyzer scanning fee keywords, salary anomalies, and Telegram/WhatsApp contacts.", body_style),
            Paragraph("Visual red warning badges preventing candidate fraud.", body_style)
        ],
        [
            Paragraph("<b>3. ATS Resume Optimizer</b>", body_style),
            Paragraph("Tokenizes candidate skill profile, matches against job requirements, and computes match % score.", body_style),
            Paragraph("Dynamic ATS PDF generation with live View & Download.", body_style)
        ],
        [
            Paragraph("<b>4. Kanban Tracker</b>", body_style),
            Paragraph("Client-side pipeline management with isolated storage keys for each authenticated user.", body_style),
            Paragraph("Applied, Interviewing, Offer stages with celebration confetti.", body_style)
        ]
    ]

    mod_table = Table(module_data, colWidths=[120, 240, 144])
    mod_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EEF2F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(mod_table)
    story.append(Spacer(1, 14))

    # Page Break for clean reading
    story.append(PageBreak())

    # ================= 4. ALGORITHMS & INNOVATION =================
    story.append(Paragraph("4. Core Algorithms & Innovation", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))

    story.append(Paragraph("<b>A. Automated Scam Detection Heuristics:</b>", h2_style))
    scam_rules = [
        "<b>Financial Exactions:</b> Checks for tokens such as 'registration fee', 'deposit', 'training fee', 'processing fee'.",
        "<b>Communication Channels:</b> Flags non-corporate domain emails (@gmail.com) and unauthorized Telegram/WhatsApp channels.",
        "<b>Salary Outlier Check:</b> Cross-references experience requirements with compensation to flag absurd work-from-home claims.",
        "<b>Trust Badge Rendering:</b> High-risk listings are labeled with <i>'★ Suspicious Listing Risk'</i> and a detailed fraud explanation."
    ]
    for r in scam_rules:
        story.append(Paragraph(f"✔ {r}", bullet_style))
    story.append(Spacer(1, 8))

    story.append(Paragraph("<b>B. ATS Resume Matching & Scoring Formula:</b>", h2_style))
    ats_rules = [
        "<b>Skill Vector Extraction:</b> Parses user skills (e.g. React, Node.js, Python, System Design) and compares with job prerequisites.",
        "<b>Jaccard Similarity / Weight:</b> <i>Score = (Candidate Skills ∩ Job Skills) / (Job Required Skills) * 100</i>.",
        "<b>Smart Resume Refactoring:</b> Injects missing industry keywords into project bullet points to maximize recruiter ATS ranking.",
        "<b>Instant PDF Compilation:</b> Generates a clean, single-column ATS-compliant document viewable directly in-app or downloadable."
    ]
    for a in ats_rules:
        story.append(Paragraph(f"✔ {a}", bullet_style))
    story.append(Spacer(1, 12))

    # ================= 5. TECH STACK TABLE =================
    story.append(Paragraph("5. Technology Stack & Specifications", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))

    tech_data = [
        [Paragraph("<b>Layer</b>", h2_style), Paragraph("<b>Technologies Used</b>", h2_style), Paragraph("<b>Justification</b>", h2_style)],
        [
            Paragraph("<b>Frontend UI</b>", body_style),
            Paragraph("HTML5, Tailwind CSS, Vanilla JS, Phosphor Icons", body_style),
            Paragraph("Sub-second initial paint, zero build overhead, responsive across mobile & desktop.", body_style)
        ],
        [
            Paragraph("<b>Mobile Runtime</b>", body_style),
            Paragraph("Capacitor 8 (Android WebView), PWA Service Worker", body_style),
            Paragraph("Native Android APK deployment without rewriting codebase in Java/Kotlin.", body_style)
        ],
        [
            Paragraph("<b>Backend / Auth</b>", body_style),
            Paragraph("Supabase Integration + Isolated LocalStorage", body_style),
            Paragraph("Supports cloud sync while guaranteeing complete client-side data privacy.", body_style)
        ],
        [
            Paragraph("<b>External APIs</b>", body_style),
            Paragraph("RapidAPI JSearch + Direct Corporate ATS Portal Links", body_style),
            Paragraph("Connects real-time live web listings with 1-click external company apply links.", body_style)
        ]
    ]
    tech_table = Table(tech_data, colWidths=[110, 210, 184])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EEF2F6")),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP')
    ]))
    story.append(tech_table)
    story.append(Spacer(1, 14))

    # ================= 6. TEACHER SUMMARY SCRIPT =================
    story.append(Paragraph("6. Teacher Viva / 2-Minute Summary Script", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))

    script_box_data = [
        [
            Paragraph(
                "<b>HOW TO EXPLAIN TO YOUR TEACHER IN 2 MINUTES:</b><br/><br/>"
                "<i>\"Respected Teacher, our project is <b>TalentAI</b>. We developed it to tackle the huge problem of fake job scams and high ATS resume rejections that college students face during placements.<br/><br/>"
                "Our application has 4 key innovations:<br/>"
                "1. <b>Verified Corporate Catalog:</b> We aggregated 102+ authentic tech jobs from top companies like Google, Swiggy, Zomato, TCS, and PhonePe with direct 1-click career portal links.<br/>"
                "2. <b>AI Scam Detection Shield:</b> It automatically flags suspicious postings asking for registration fees or redirecting to Telegram, protecting students from fraud.<br/>"
                "3. <b>ATS Resume Optimizer:</b> It calculates exact skill match percentages and automatically generates ATS-friendly PDF resumes that students can preview and download.<br/>"
                "4. <b>Application Tracker:</b> A full Kanban tracking pipeline with celebratory confetti and milestone reminders.<br/><br/>"
                "We built this as a high-performance cross-platform system, packaged as an Android APK using Capacitor, and deployed live at <b>https://talentai-rohan.surge.sh</b>.\"</i>",
                callout_style
            )
        ]
    ]
    script_table = Table(script_box_data, colWidths=[504])
    script_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#F1F5F9")),
        ('BOX', (0,0), (-1,-1), 1.5, ACCENT),
        ('LEFTPADDING', (0,0), (-1,-1), 14),
        ('RIGHTPADDING', (0,0), (-1,-1), 14),
        ('TOPPADDING', (0,0), (-1,-1), 12),
        ('BOTTOMPADDING', (0,0), (-1,-1), 12),
        ('ROUNDEDCORNERS', [6, 6, 6, 6])
    ]))
    story.append(script_table)
    story.append(Spacer(1, 14))

    # ================= 7. CONCLUSION & FUTURE SCOPE =================
    story.append(Paragraph("7. Results & Future Roadmap", h1_style))
    story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceBefore=2, spaceAfter=8))
    results_text = (
        "<b>Current Status:</b> TalentAI is 100% functional, responsive across mobile & desktop devices, verified with 102 active corporate roles, "
        "and deployed publicly for live demonstration.<br/>"
        "<b>Future Enhancements:</b> (1) AI Mock Interview Bot with real-time audio analysis, (2) Direct recruiter Supabase chat dashboard, and (3) Automated email calendar integration for scheduled interview rounds."
    )
    story.append(Paragraph(results_text, body_style))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"Successfully generated PDF report: {pdf_filename}")

if __name__ == "__main__":
    build_pdf()
