import gradio as gr
import requests

API_URL = "https://www.themealdb.com/api/json/v1/1/filter.php?i="
LOOKUP_URL = "https://www.themealdb.com/api/json/v1/1/lookup.php?i="

def buscar_receita(ingredientes):
    ingredientes = ingredientes.lower().replace(",", "%2C")
    resposta = requests.get(API_URL + ingredientes)

    if resposta.status_code != 200 or not resposta.json()["meals"]:
        return "No recipes found with these ingredients. Try others! (Enter in English, e.g., chicken, rice)"

    receita = resposta.json()["meals"][0]  
    nome = receita["strMeal"]
    imagem = receita["strMealThumb"]
    id_receita = receita["idMeal"]

    detalhes = requests.get(LOOKUP_URL + id_receita).json()["meals"][0]
    instrucoes = detalhes["strInstructions"][:500] + "..."  
    link = detalhes["strSource"] or detalhes["strYoutube"] or ""

    resposta_formatada = f"🍽 Suggested recipe: **{nome}**\n\n👨‍🍳 Instructions: {instrucoes}\n\n🔗 [View full recipe]({link})"
    return resposta_formatada

iface = gr.Interface(
    fn=buscar_receita,
    inputs=gr.Textbox(label="Enter ingredients (in English, separated by commas)", placeholder="E.g., chicken, rice, tomato"),
    outputs="markdown",
    title="Recipe Chatbot",
    description="Get recipe suggestions based on the ingredients you provide (in English). Source: TheMealDB API",
)

if __name__ == "__main__":
    iface.launch(share=True)
