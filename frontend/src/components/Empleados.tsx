import type { Empleado } from "../types"

type EmpleadosProps = {
    datos: Empleado
}

export default function Empleados({datos}: EmpleadosProps) {
  return (
    <>
    {/* Mostrar datos de ejemplo */}
        <li key={datos.id}>
            {datos.nombre} {datos.apellido} - {datos.correo} ({datos.puesto})
        </li>
    </>
  )
}
