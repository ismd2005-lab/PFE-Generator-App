import streamlit as st
import time
from fpdf import FPDF
import tempfile


# --- MOTEUR PDF "RENAISSANCE" (Adapté Technique) ---
class PDF(FPDF):
    def header(self):
        pass

    def footer(self):
        self.set_y(-20)
        self.set_font('Times', 'I', 10)  # Police Times (Serif)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, 'Document généré par le Générateur PFE - 2026', 0, 0, 'C')


def create_artistic_pdf(data, instructions, logo_file):
    pdf = PDF()
    pdf.add_page()

    # --- 1. PALETTE DE COULEURS ---
    text_r, text_g, text_b = 20, 20, 20  # Noir Encre
    accent_r, accent_g, accent_b = 160, 82, 45  # Sienne (Terre brûlée)

    instr = instructions.lower() if instructions else ""
    if "bleu" in instr:
        accent_r, accent_g, accent_b = 25, 25, 112
    elif "rouge" in instr:
        accent_r, accent_g, accent_b = 139, 0, 0
    elif "vert" in instr:
        accent_r, accent_g, accent_b = 85, 107, 47

    # --- 2. CADRE ---
    pdf.set_draw_color(text_r, text_g, text_b)
    pdf.set_line_width(0.5)
    pdf.rect(10, 10, 190, 277)

    pdf.set_draw_color(accent_r, accent_g, accent_b)
    pdf.set_line_width(1)
    pdf.rect(12, 12, 186, 273)

    # --- 3. EN-TÊTE ---
    if logo_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp_file:
            tmp_file.write(logo_file.getvalue())
            tmp_path = tmp_file.name
        try:
            pdf.image(tmp_path, x=95, y=20, w=20)
        except:
            pass
        pdf.set_y(45)
    else:
        pdf.set_y(30)

    # Université
    pdf.set_font("Times", 'B', 16)
    pdf.set_text_color(text_r, text_g, text_b)
    univ = data.get('univ', '').upper().encode('latin-1', 'replace').decode('latin-1')
    univ_spaced = " ".join(list(univ))
    pdf.multi_cell(0, 8, univ_spaced, 0, 'C')

    pdf.ln(2)
    pdf.set_font("Times", 'I', 14)
    pdf.set_text_color(accent_r, accent_g, accent_b)
    filiere = data.get('filiere', '').encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(0, 8, filiere, 0, 1, 'C')

    # Séparateur
    pdf.set_draw_color(150, 150, 150)
    pdf.line(80, pdf.get_y() + 5, 130, pdf.get_y() + 5)

    # --- 4. LE TITRE ---
    pdf.set_y(90)
    titre = data.get('titre', '').encode('latin-1', 'replace').decode('latin-1')

    # Titre en très gros Serif
    pdf.set_font("Times", 'B', 26)
    pdf.set_text_color(text_r, text_g, text_b)

    # Titre centré
    pdf.multi_cell(170, 12, titre, border=0, align='C')

    # Sous-titre
    pdf.ln(10)
    pdf.set_font("Times", 'I', 12)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 10, "Mémoire présenté pour l'obtention du Diplôme d'Ingénieur d'État", 0, 1, 'C')

    # --- 5. COMPOSITION (Noms) ---
    pdf.set_y(150)

    # Auteur (Gauche)
    pdf.set_xy(30, 150)
    pdf.set_font("Times", '', 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(60, 6, "Réalisé par :", 0, 1, 'L')

    pdf.set_xy(30, 158)
    pdf.set_font("Times", 'B', 14)
    pdf.set_text_color(text_r, text_g, text_b)
    auteur = data.get('auteur', '').encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(70, 6, auteur, 0, 'L')

    # Encadrant (Droite)
    pdf.set_xy(120, 150)
    pdf.set_font("Times", '', 12)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(60, 6, "Encadré par :", 0, 1, 'L')

    pdf.set_xy(120, 158)
    pdf.set_font("Times", 'B', 14)
    pdf.set_text_color(text_r, text_g, text_b)
    encadrant = data.get('encadrant', '').encode('latin-1', 'replace').decode('latin-1')
    pdf.multi_cell(70, 6, encadrant, 0, 'L')

    # --- 6. LE JURY ---
    if data.get('jury'):
        pdf.set_y(200)
        pdf.set_font("Times", 'B', 12)
        pdf.set_text_color(accent_r, accent_g, accent_b)
        pdf.cell(0, 10, "Composition du Jury", 0, 1, 'C')

        pdf.set_font("Times", '', 11)
        pdf.set_text_color(40, 40, 40)
        jury_txt = data.get('jury', '').split(',')

        y_pos = 210
        for membre in jury_txt:
            membre = membre.strip().encode('latin-1', 'replace').decode('latin-1')
            pdf.set_xy(40, y_pos)
            pdf.cell(130, 6, f"{membre}", 0, 1, 'C')
            y_pos += 6

    # --- 7. PIED DE PAGE (SANS QR CODE) ---
    pdf.set_y(255)
    pdf.set_draw_color(accent_r, accent_g, accent_b)
    pdf.line(50, 255, 160, 255)

    pdf.set_y(260)
    pdf.set_font("Times", 'B', 14)
    pdf.set_text_color(text_r, text_g, text_b)
    pdf.cell(0, 10, "Année Universitaire 2025 - 2026", 0, 0, 'C')

    return pdf.output(dest='S').encode('latin-1')


# --- CONFIGURATION STREAMLIT ---
st.set_page_config(page_title="Générateur PFE", page_icon="🎓", layout="centered")

st.markdown("<h1 style='text-align: center; font-family: Times New Roman;'>🎓 Générateur de Page de Garde PFE</h1>",
            unsafe_allow_html=True)

st.markdown(
    "<p style='text-align: center; font-style: italic; color: gray;'>« Les détails font la perfection, et la perfection n'est pas un détail. » — Léonard de Vinci</p>",
    unsafe_allow_html=True)
st.markdown("---")

# --- BARRE LATÉRALE ---
with st.sidebar:
    st.header("⚙️ Configuration")
    format_sortie = st.radio("Format de sortie :", ("PDF Standard", "LaTeX (Code Source)"))
    mode_demo = st.toggle("Mode Gratuit", value=True)
    st.markdown("---")
    uploaded_logo = st.file_uploader("Logo Établissement (Optionnel)", type=['png', 'jpg'])

    api_key = ""
    if not mode_demo:
        api_key = st.text_input("Clé API", type="password")

try:
    from openai import OpenAI
except ImportError:
    pass


# --- FONCTION GENERATION ---
def generate_latex(data, instructions):
    return r"""
\documentclass[12pt, a4paper]{report}
\usepackage{times}
\begin{document}
    \begin{center}
        \huge \textbf{""" + data['titre'] + r"""}
    \end{center}
\end{document}
"""


# --- INTERFACE ---
col1, col2 = st.columns(2)
with col1:
    univ = st.text_input("🏛️ Établissement / Université", placeholder="Ex: ENSA Oujda")
    filiere = st.text_input("🎓 Filière", placeholder="Ex: Génie Informatique")
    titre = st.text_input("📝 Intitulé du Sujet", placeholder="Ex: Optimisation des Réseaux de Neurones")

with col2:
    auteur = st.text_input("👤 Réalisé par", placeholder="Votre Nom")
    encadrant = st.text_input("👨‍🏫 Encadré par", placeholder="Ex: Pr. BOUCHENTOUF")
    # SUPPRESSION DE LA CASE LIEN ICI

st.markdown("**⚖️ Membres du Jury :**")
jury = st.text_area("Liste des membres", placeholder="Pr. Nom1, Pr. Nom2...", height=68)

st.markdown("**🎨 Personnalisation (Prompt Couleur) :**")
instructions = st.text_input("Couleur dominante (ex: 'Rouge', 'Bleu', 'Vert')",
                             placeholder="Laissez vide pour le style classique")

if st.button("✨ GÉNÉRER LE DOCUMENT ✨", use_container_width=True):
    if not titre or not auteur:
        st.error("⚠️ Veuillez renseigner le Titre et l'Auteur.")
    else:
        data_user = {
            "univ": univ, "filiere": filiere, "titre": titre,
            "auteur": auteur, "encadrant": encadrant, "jury": jury
        }

        with st.spinner("Génération du rapport en cours..."):
            try:
                if "LaTeX" in format_sortie:
                    content = generate_latex(data_user, instructions)
                    st.code(content, language='latex')
                else:
                    # APPEL SANS QR CODE
                    pdf_bytes = create_artistic_pdf(data_user, instructions, uploaded_logo)
                    st.balloons()
                    st.success("Document généré avec succès.")
                    st.download_button(
                        label="📥 TÉLÉCHARGER LE PDF",
                        data=pdf_bytes,
                        file_name="page_de_garde_pfe.pdf",
                        mime="application/pdf"
                    )
            except Exception as e:
                st.error(f"Erreur : {e}")
