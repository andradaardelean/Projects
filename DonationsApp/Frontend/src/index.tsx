import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';

import './index.css';
//import "antd/dist/reset.css";
import { BrowserRouter } from 'react-router-dom';
import BaseRoutes from './BaseRoutes';
import { QueryClient, QueryClientProvider } from 'react-query';

const container = document.getElementById('root'); //ia div-ul root din index.html

//configuratie default pt react query
const queryClient = new QueryClient({
  defaultOptions: {
    queries: {
      retry: false
    }
  }
});

if (!container) {
  throw new Error("React root element doesn't exist!");
}

const root = createRoot(container);

root.render(
  <StrictMode>
    <QueryClientProvider client={queryClient}>
      <BrowserRouter>
        <BaseRoutes />
      </BrowserRouter>
    </QueryClientProvider>
  </StrictMode>
);
