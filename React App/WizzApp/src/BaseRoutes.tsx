import React from "react";
import { Routes, Route, Navigate } from "react-router";
import FlightPage from "./pages/FlightPage";

import LandingPage from "./pages/LandingPage";

const BaseRoutes: React.FC = () => {
  return (
    <Routes>
      <Route path="/" index element={<LandingPage />} />
      <Route path="/flights" element={<FlightPage />} />
      <Route path="*" element={<Navigate to="/" />} />
    </Routes>
  );
};

export default BaseRoutes;