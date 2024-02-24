# Stage 1: Base
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
ENV ASPNETCORE_URLS=http://*:12500
EXPOSE 12500

# Stage 2: Build
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
COPY AuthService/ /app/AuthService/
RUN dotnet restore /app/AuthService/AuthService.WebApi/AuthService.WebApi.csproj
WORKDIR /app/AuthService/AuthService.WebApi
RUN dotnet build AuthService.WebApi.csproj -c Release -o /app/build --no-restore

# Stage 3: Publish
FROM build AS publish
RUN dotnet publish AuthService.WebApi.csproj -c Release -o /app/publish --no-restore

# Stage 4: Final
FROM base AS final
WORKDIR /app
ENV COMPlus_EnableDiagnostics=0
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "AuthService.WebApi.dll"]
