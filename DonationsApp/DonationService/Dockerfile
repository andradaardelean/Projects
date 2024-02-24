# Stage 1: Base
FROM mcr.microsoft.com/dotnet/aspnet:6.0 AS base
ENV ASPNETCORE_URLS=http://*:12700

# Stage 2: Build
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
COPY DonationService/ /app/DonationService/
RUN dotnet restore /app/DonationService/DonationService.WebApi/DonationService.WebApi.csproj
WORKDIR /app/DonationService/DonationService.WebApi
RUN dotnet build DonationService.WebApi.csproj -c Release -o /app/build --no-restore

# Stage 3: Publish
FROM build AS publish
RUN dotnet publish DonationService.WebApi.csproj -c Release -o /app/publish --no-restore

# Stage 4: Final
FROM base AS final
WORKDIR /app
ENV COMPlus_EnableDiagnostics=0
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DonationService.WebApi.dll"]
