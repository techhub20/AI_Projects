# Stage 1: Build the Angular app
FROM node:18 AS builder
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build --prod
RUN ls -al /app/dist/resumeanalyser-frontend

# Stage 2: Serve the app with Nginx
FROM nginx:alpine
COPY --from=builder /app/dist/resumeanalyser-frontend/browser /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]

