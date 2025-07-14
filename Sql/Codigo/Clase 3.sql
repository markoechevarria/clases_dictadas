USE semana2;
SELECT * FROM inventario;
 
-- FUNCIONES ESCALARES
-- TEXTO

-- UPPER(campo) - Convierte a may�sculas.
SELECT UPPER(categoria) FROM inventario;

-- LOWER(campo) - Convierte a min�sculas.
SELECT LOWER(categoria) FROM inventario;

-- LEN(campo) - Longitud del texto.
SELECT LEN(categoria) FROM inventario;

-- SUBSTRING(campo, inicio, longitud) - Extrae una parte del texto.
SELECT SUBSTRING(categoria,2,4) FROM inventario;

-- FECHA Y HORA

-- GETDATE() - Fecha y hora actual.
SELECT GETDATE();

-- YEAR(campo_fecha) - A�o de una fecha.
SELECT YEAR(fecha_ingreso) FROM inventario;
SELECT MONTH(fecha_ingreso) FROM inventario;
SELECT DAY(fecha_ingreso) FROM inventario;

-- CONVERT(tipo_dato, campo_fecha, codigo_tipo_fecha)
SELECT fecha_ingreso FROM inventario;
SELECT CONVERT(VARCHAR, fecha_ingreso, 112) FROM inventario;

-- NUMERICAS

-- ROUND(campo, decimales) - Redondea un n�mero.
SELECT precio FROM inventario;
SELECT ROUND(precio, 1) FROM inventario;

-- ABS(campo) - Valor absoluto.
SELECT stock FROM inventario;
SELECT ABS(stock) FROM inventario;

-- FLOOR(campo) - Redondeo hacia arriba o abajo.
SELECT precio FROM inventario;
SELECT FLOOR(precio) FROM inventario;


-- Comparaciones m�ltiples: OR, AND
SELECT * FROM inventario;
SELECT * FROM inventario WHERE stock<40;
SELECT * FROM inventario WHERE stock<40 AND precio>250;

SELECT * FROM inventario;
SELECT * FROM inventario WHERE stock<40 OR precio<25;

-- Nulos: IS NULL, IS NOT NULL

SELECT * FROM inventario;
SELECT * FROM inventario WHERE categoria IS NULL;
SELECT * FROM inventario WHERE categoria IS NOT NULL;

-- FUNCIONES DE AGREGACION
-- Combinan valores de multiples filas en un solo resultado

-- SUM(campo) - Suma total
SELECT * FROM inventario;
SELECT SUM(stock) FROM inventario;

-- AVG(campo) � Promedio
SELECT AVG(stock) FROM inventario;

-- MIN(campo) - Valor m�nimo
SELECT MIN(stock) FROM inventario;

-- MAX(campo) - Valor m�ximo
SELECT MAX(stock) FROM inventario;

-- COUNT(campo) - N�mero de registros.
SELECT COUNT(stock) FROM inventario WHERE stock>10;

SELECT * FROM inventario;

-- GROUP BY: Agrupa filas que tienen valores en com�n.
SELECT categoria, COUNT(*) AS 'Cantidad de registros', SUM(stock) AS 'Stock total' FROM inventario GROUP BY categoria;

-- HAVING: Filtra resultados despu�s de aplicar funciones de agregaci�n.
SELECT * FROM inventario;
SELECT categoria, COUNT(*) AS 'Cantidad', SUM(stock) AS 'Stock total' FROM inventario GROUP BY categoria HAVING SUM(stock)>50;
SELECT categoria, SUM(precio) AS 'Precio' FROM inventario GROUP BY categoria HAVING SUM(precio)<100;

/*
EJERCICIO 1
Usa la tabla productos y la tabla ventas con los siguientes esquemas:
	Tabla productos:
		id_producto (entero, clave primaria)
		nombre (texto, 100 caracteres)
		categoria (texto, 50 caracteres)
		precio (decimal, 2 decimales)
	Tabla ventas:
		id_venta (entero, clave primaria)
		id_producto (entero, clave for�nea)
		cantidad (entero)
		fecha_venta (fecha)
Inserta registros de ejemplo en ambas tablas con al menos 10 productos y 20 ventas.
Realiza las siguientes consultas:
	Calcula el total de ingresos generados por cada categor�a de producto.
	Encuentra la categor�a con mayores ingresos totales.
	Muestra los productos que tuvieron ventas por un total mayor al promedio de ingresos por producto.
	Encuentra el d�a con las ventas totales m�s altas.
*/

CREATE TABLE productos_ejercicio (
	id_producto INT,
	nombre VARCHAR(100),
	categoria VARCHAR(50),
	precio FLOAT
)
CREATE TABLE ventas_ejercicio (
	id_venta INT,
	id_producto INT,
	cantidad INT,
	fecha_venta DATE
)

INSERT INTO productos_ejercicio (id_producto, nombre, categoria, precio) VALUES
(1, 'Laptop', 'Electr�nica', 1200.00),
(2, 'Smartphone', 'Electr�nica', 800.00),
(3, 'Auriculares', 'Accesorios', 150.00),
(4, 'Teclado mec�nico', 'Accesorios', 100.00),
(5, 'Monitor', 'Electr�nica', 300.00),
(6, 'Mouse inal�mbrico', 'Accesorios', 25.00),
(7, 'C�mara de seguridad', 'Hogar', 200.00),
(8, 'Smartwatch', 'Electr�nica', 180.00),
(9, 'Cargador inal�mbrico', 'Accesorios', 40.00),
(10, 'Altavoces Bluetooth', 'Accesorios', 70.00);

INSERT INTO ventas_ejercicio (id_venta, id_producto, cantidad, fecha_venta) VALUES
(1, 1, 2, '2025-01-10'),
(2, 2, 5, '2025-01-11'),
(3, 3, 3, '2025-01-12'),
(4, 4, 1, '2025-01-13'),
(5, 5, 4, '2025-01-14'),
(6, 6, 7, '2025-01-15'),
(7, 7, 2, '2025-01-16'),
(8, 8, 1, '2025-01-17'),
(9, 9, 6, '2025-01-18'),
(10, 10, 3, '2025-01-19'),
(11, 1, 1, '2025-01-20'),
(12, 2, 2, '2025-01-21'),
(13, 3, 4, '2025-01-22'),
(14, 4, 3, '2025-01-23'),
(15, 5, 5, '2025-01-24'),
(16, 6, 2, '2025-01-25'),
(17, 7, 1, '2025-01-26'),
(18, 8, 3, '2025-01-27'),
(19, 9, 5, '2025-01-28'),
(20, 10, 4, '2025-01-29');

SELECT * FROM productos_ejercicio;
SELECT * FROM ventas_ejercicio;

-- Calcula el total de ingresos generados por cada categor�a de producto.
SELECT categoria, SUM(precio) FROM productos_ejercicio GROUP BY categoria; 

-- Encuentra la categor�a con mayores ingresos totales.
SELECT TOP 1 categoria, SUM(precio) AS 'Precio total' FROM productos_ejercicio GROUP BY categoria ORDER BY SUM(precio) DESC;

-- Muestra los productos que tuvieron ventas por un total mayor al promedio de ingresos por producto.
SELECT * FROM productos_ejercicio;
SELECT * FROM productos_ejercicio WHERE precio > (SELECT AVG(precio) FROM productos_ejercicio);

-- Encuentra el d�a con la mayor cantidad de ventas.
SELECT * FROM ventas_ejercicio;
SELECT TOP 1 fecha_venta, SUM(cantidad) AS 'Cantidad ventas' FROM ventas_ejercicio GROUP BY fecha_venta ORDER BY SUM(cantidad) DESC;


/*
Usa las tablas clientes y pedidos con los siguientes esquemas:
	Tabla clientes:
		id_cliente (entero, clave primaria)
		nombre (texto, 100 caracteres)
		email (texto, 100 caracteres)
	Tabla pedidos:
		id_pedido (entero, clave primaria)
		id_cliente (entero, clave for�nea)
		fecha_pedido (fecha)
		total (decimal, 2 decimales)
Inserta al menos 8 clientes y 15 pedidos
Realiza las siguientes consultas:
	Muestra los pedidos agrupados por fecha, con el total de pedidos y el ingreso total.
*/

CREATE TABLE clientes_ejercicio (
	id_cliente INT,
	nombre VARCHAR(100),
	email VARCHAR(100)
);
CREATE TABLE pedidos_ejercicio (
	id_pedido INT,
	id_cliente INT,
	fecha_pedido DATE,
	total FLOAT
);

INSERT INTO clientes_ejercicio (id_cliente, nombre, email) VALUES
(1, 'Juan P�rez', 'juan.perez@email.com'),
(2, 'Ana G�mez', 'ana.gomez@email.com'),
(3, 'Luis Rodr�guez', 'luis.rodriguez@email.com'),
(4, 'Maria Fern�ndez', 'maria.fernandez@email.com'),
(5, 'Carlos Mart�nez', 'carlos.martinez@email.com'),
(6, 'Laura L�pez', 'laura.lopez@email.com'),
(7, 'Pedro S�nchez', 'pedro.sanchez@email.com'),
(8, 'Sofia Herrera', 'sofia.herrera@email.com'),
(9, 'Ra�l Gonz�lez', 'raul.gonzalez@email.com'),
(10, 'Isabel D�az', 'isabel.diaz@email.com');

INSERT INTO pedidos_ejercicio (id_pedido, id_cliente, fecha_pedido, total) VALUES
(1, 1, '2025-02-10', 150.75),
(2, 2, '2025-03-11', 245.50),
(3, 3, '2025-02-12', 99.99),
(4, 4, '2025-02-13', 380.00),
(5, 5, '2025-02-14', 210.25),
(6, 6, '2025-03-15', 320.40),
(7, 7, '2025-03-16', 500.00),
(8, 8, '2025-04-17', 120.50),
(9, 9, '2025-04-18', 275.30),
(10, 10, '2025-04-19', 450.00);

-- Muestra los pedidos agrupados por fecha, con el total de pedidos y el ingreso total.

SELECT * FROM pedidos_ejercicio;
SELECT TOP 5 fecha_pedido, COUNT(*) AS 'Cantidad de pedidos por fecha',  SUM(total) AS 'Ingreso total' FROM pedidos_ejercicio GROUP BY fecha_pedido ORDER BY SUM(total) DESC;