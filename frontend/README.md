# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Babel](https://babeljs.io/) (or [oxc](https://oxc.rs) when used in [rolldown-vite](https://vite.dev/guide/rolldown)) for Fast Refresh
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/) for Fast Refresh

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

## **Frontend Setup & Running the App**
### **Prerequisites**
Make sure you have the following installed
* Node.js(v18 or newer recommended)
* npm(comes with Node)
You can verify with 
```bash
node -v
npm -v
```

### **1. Installing Dependencies**
Install dependencies
```bash
cd frontend
npm install
```

### **2. Running the Development Server**
Start the Vite development server
```bash
npm run dev
```
You should see output similar to
```bash
Local: http://localhost:5173/
```

### **3. Backend Requirment**
The frontend expects the backend Flask server to be running at
```bash
http://localhost:8000
```
Make sure the backend is running before making API requests from the frontend