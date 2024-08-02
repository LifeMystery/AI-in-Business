import { defineConfig } from 'vite';

export default defineConfig({
  build: {
    outDir: 'public', // Output directory for the built files
    rollupOptions: {
      input: {
        main: 'public/index.html',  // Entry point for index.html
        dashboard: 'public/dashboard.html',  // Entry point for dashboard.html
      },
    },
  },
});
