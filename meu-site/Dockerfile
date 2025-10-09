# Imagem base
FROM node:20-alpine

# Define diretório de trabalho
WORKDIR /usr/src/app

# Copia package.json e instala dependências
COPY package*.json ./
RUN npm install --production

# Copia o código da aplicação
COPY . .

# Expõe a porta usada pela aplicação
EXPOSE 3000

# Comando padrão de inicialização
CMD ["npm", "start"]
