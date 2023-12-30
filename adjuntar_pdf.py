# LLIBRERIES UTILITZADES 

import streamlit as st
import PyPDF2


# DEFINICIÓ DE VARIABLES I DESENVOLUPAMENT DE LES FUNCIONS ENCARREGADES D'UNIR ARXIUS .PDF

output_pdf = "documents/archivo_adjuntado.pdf"

def unir_pdf(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()

    for document in documents:
        pdf_final.append(document)

    pdf_final.write(output_path)


# DESENVOLUPAMENT DE LA PART GRÀFICA DEL SCRIPT

st.header("UNIÓ D'ARXIUS PDF")
st.subheader("")
st.text("""
Feu clic al botó de 'Browse' per cercar i seleccionar els arxius .PDF a unir. 
Posteriorment premeu el botó de 'Unir PDF' perquè s'executi l'acció.
""")

pdf_seleccionados = st.file_uploader(label="", accept_multiple_files=True)

pdf_unir = st.button(label="Unir PDF")


# DESENVOLUPAMENT DEL RETORN DE L'ARXIU AMB ELS PDF'S AJUNTATS

if pdf_unir: 

    if len(pdf_seleccionados) <= 1:
        st.warning("Has d'adjuntar un mínim de dos archius .PDF")

    else:
        unir_pdf(output_pdf, pdf_seleccionados)
        st.success("Aquí has de descarregar el archiu .PDF final")
        with open(output_pdf, 'rb') as file:
            pdf_data = file.read()
        st.download_button(label="Descarregar PDF final", data=pdf_data, file_name="pdf_final.pdf")