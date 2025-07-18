import { useEffect, useState } from "react";
import Empleados from "./components/Empleados";
import type { Empleado } from "./types";

function App() {
  const [empleados, setEmpleados] = useState<Empleado[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((res) => res.json())
      .then((data) => setEmpleados(data.message));
  }, []);

  return (
    <div className="bg-gradient-to-t from-purple-900 to-purple-500 h-auto min-h-screen w-full mx-auto flex flex-col xl:flex-row items-center justify-center">
      <div className="bg-white border rounded-lg shadow-lg p-6 w-full max-w-3xl">
        <h1>Lista de empleados</h1>
        <div>
          {empleados.map((empleado) => (
            <Empleados key={empleado.id} datos={empleado} />
          ))}
        </div>
      </div>
    </div>
  );
}

export default App;
