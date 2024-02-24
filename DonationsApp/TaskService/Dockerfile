# Stage 1: Base
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
ENV ASPNETCORE_URLS=http://*:12800

# Stage 2: Build
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
COPY TaskService/ /app/TaskService/
RUN dotnet restore /app/TaskService/TaskService.WebApi/TaskService.WebApi.csproj
WORKDIR /app/TaskService/TaskService.WebApi
RUN dotnet build TaskService.WebApi.csproj -c Release -o /app/build --no-restore

# Stage 3: Publish
FROM build AS publish
RUN dotnet publish TaskService.WebApi.csproj -c Release -o /app/publish --no-restore

# Stage 4: Final
FROM base AS final
WORKDIR /app
ENV COMPlus_EnableDiagnostics=0
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "TaskService.WebApi.dll"]
