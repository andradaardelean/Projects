# Stage 1: Base
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
ENV ASPNETCORE_URLS=http://*:12600

# Stage 2: Build
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
COPY LocationService/ /app/LocationService/
RUN dotnet restore /app/LocationService/LocationService.WebApi/LocationService.WebApi.csproj
WORKDIR /app/LocationService/LocationService.WebApi
RUN dotnet build LocationService.WebApi.csproj -c Release -o /app/build --no-restore

# Stage 3: Publish
FROM build AS publish
RUN dotnet publish LocationService.WebApi.csproj -c Release -o /app/publish --no-restore

# Stage 4: Final
FROM base AS final
WORKDIR /app
ENV COMPlus_EnableDiagnostics=0
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "LocationService.WebApi.dll"]
