export type Response = {
    productos : Producto[];
}

export type Producto = {
    id_producto:     string;
    nombre:          string;
    marca:           string;
    precio:          string;
    descripcion:     string;
    cantidad:        number;
    talla:           string;
    color:           string;
    genero:          string;
    estado:          number;
    img:             string;
    id_proveedor:    number;
    id_subcategoria: number;
    id_estante:      number;
}

