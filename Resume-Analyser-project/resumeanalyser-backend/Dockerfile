# Build stage
FROM maven:3.8.5-eclipse-temurin-17 AS build

# Set the working directory to /app
WORKDIR /app

# Copy all files from the current directory to the container's /app directory
COPY . .

# Build the application using Maven, skipping tests
RUN mvn clean package -DskipTests

# Run stage
FROM eclipse-temurin:17

# Set the working directory to /app
WORKDIR /app

# Install curl to fetch wait-for-it.sh script
RUN apt-get update && apt-get install -y curl

# Download the wait-for-it.sh script
RUN curl -o /app/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && chmod +x /app/wait-for-it.sh

# Copy the JAR file from the build stage
COPY --from=build /app/target/*.jar app.jar

# Expose port 8080 to allow communication to/from the container
EXPOSE 8080

# Use wait-for-it.sh to wait for MySQL (or any service) to be available
# Replace 'resumeanalyser-db:3306' with the actual hostname and port you want to wait for
ENTRYPOINT ["./wait-for-it.sh", "resumeanalyser-db:3306", "--", "java", "-jar", "app.jar"]



# # Build stage
# FROM maven:3.8.5-eclipse-temurin-17 AS build
# WORKDIR /app
# COPY . .
# RUN mvn clean package -DskipTests

# # Run stage
# FROM eclipse-temurin:17
# WORKDIR /app
# COPY --from=build /app/target/*.jar app.jar
# EXPOSE 8080
# ENTRYPOINT ["java", "-jar", "app.jar"]
