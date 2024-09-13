# swarm_ai_agents
Agency Idea: 


1. Input text que establece un requerimiento de software a alto nivel y lo transforma a US y lo crea en Azure -> devuelve el ID del Azure ITEM
2. Otro agente crea un mockup usando DALL-E y comenta en el AZURE ITEM. -> devuelve la imagen. 
3. Agente que transforma la imagen en HTML -> devuelve un JSON con 3 atributos (algo así)::

{
    "azure_id": "TEST-321123",
  "html": "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n    <link rel=\"stylesheet\" href=\"style.css\">\n    <title>Drawing Game</title>\n</head>\n<body>\n    <div class=\"game-container\">\n        <div class=\"scoreboard\">\n            <h2>Round 4 of 4</h2>\n            <p>Current Player: <span id=\"current-player\">José</span></p>\n            <p>Points: <span id=\"player-points\">2020</span></p>\n        </div>\n        <div class=\"drawing-area\">\n            <canvas id=\"drawingCanvas\" width=\"600\" height=\"400\"></canvas>\n            <div class=\"cloud\"><div class=\"cloud-body\"></div><div class=\"lightning\"></div></div>\n        </div>\n        <div class=\"chat\">\n            <div class=\"messages\" id=\"message-box\">\n                <p>José: guessed the word!</p>\n                <p>José: The word is drawing now!</p>\n                <p>Maria: tormenta</p>\n                <p>Antonio: tormenta</p>\n                <p>José: tormenta</p>\n            </div>\n            <input type=\"text\" id=\"message-input\" placeholder=\"Type your message...\">\n            <button id=\"send-button\">Send</button>\n        </div>\n    </div>\n    <script src=\"script.js\"></script>\n</body>\n</html>",
  "css": "body {\n    font-family: Arial, sans-serif;\n    background-color: #e0e0e0;\n    margin: 0;\n}\n\n.game-container {\n    width: 640px;\n    margin: 0 auto;\n    background-color: #fff;\n    border: 2px solid #000;\n    border-radius: 5px;\n    box-shadow: 0 0 10px rgba(0,0,0,0.1);\n}\n\n.scoreboard {\n    padding: 10px;\n    background: #007bff;\n    color: white;\n    text-align: center;\n}\n\ndrawing-area {\n    position: relative;\n    border: 1px solid #ccc;\n}\n\n#drawingCanvas {\n    width: 100%;\n    height: 100%;\n}\n\n.cloud {\n    position: absolute;\n    top: 50%;\n    left: 50%;\n    transform: translate(-50%, -50%);\n    width: 120px;\n    height: 70px;\n    background: #aaa;\n    border-radius: 50px;\n}\n\n.cloud-body {\n    width: 100%;\n    height: 100%;\n    background-color: #ffffff;\n    border-radius: 50%;\n    position: relative;\n}\n\n.lightning {\n    position: absolute;\n    bottom: -40px;\n    left: 50%;\n    transform: translateX(-50%);\n    width: 0;\n    height: 0;\n    border-left: 10px solid transparent;\n    border-right: 10px solid transparent;\n    border-top: 50px solid yellow;\n}\n\n.chat {\n    padding: 10px;\n    border-top: 2px solid #007bff;\n}\n\n#message-box {\n    max-height: 100px;\n    overflow-y: scroll;\n    margin-bottom: 10px;\n}\n\n#message-input {\n    width: 80%;\n}\n\n#send-button {\n    width: 15%;\n}",
  "javascript": "document.getElementById('send-button').addEventListener('click', function() {\n    const input = document.getElementById('message-input');\n    const messageBox = document.getElementById('message-box');\n    const message = input.value;\n    if (message) {\n        const newMessage = document.createElement('p');\n        newMessage.textContent = 'You: ' + message;\n        messageBox.appendChild(newMessage);\n        input.value = '';\n        messageBox.scrollTop = messageBox.scrollHeight;\n    }\n});"
}

4. Agente que toma el JSON y GENERA 3 archivos, usando el azure_id anterior. Por ejemplo TEST-321123.css, TEST-321123.js y TEST-321123.html. Este agente ejecuta un servido ngix 



## PROMPTS de ayuda 

Create a visually stunning and user-friendly product page for an e-commerce platform. The design should include a large product image section, product title, price, description, customer reviews, and an 'Add to Cart' button. The layout should be modern, clean, and easy to navigate, with a focus on enhancing the shopping experience. Include sections for related products and promotional banners. Use a color scheme that is appealing and suitable for a wide range of products. Generate HTML CSS and JS of this image.  


## Comandos 

 agency-swarm create-agent-template --name "FrontendDeveloperAgent" --description "This agent takes a picture reads it, undestands it, and generate 3 files (html js and css) that represent this image"

## TODO: 
no funciona con png ? ir mirando eso. No lo entiendo porque parecía que funcionaba copy pasteando una imagen. 
Hay que ver cómo hacer también que los input fields estén validados.
Creo que al final no se puede usar un BASE_TOOL para utilizar el structured output (response_format)
https://stackoverflow.com/questions/78875261/azure-openai-gpt-4o-mini-structured-outputs-response-format-not-working#comment139065235_78875261

[] Ya funciona 
[] Usar Devid para guardar los archivos css js y html
