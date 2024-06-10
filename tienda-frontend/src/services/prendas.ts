export const getProductoById = async ({id}) => {
    try {
        const res = await fetch(`http://127.0.0.1:8000/api/catalogo/productos/${id}/`);
        const productId = await res.json();
        return productId;
    } catch (error) {
        throw new Error(`Error al obtener los datos - ${error}`);
    }
}

export const getAllProductos = async () => {
    try {
        const res = await fetch(`http://127.0.0.1:8000/api/catalogo/productos/`);
        const products = await res.json();
        return products;
    } catch (error) {
        throw new Error(`Error al obtener los datos - ${error}`);
    }
}
