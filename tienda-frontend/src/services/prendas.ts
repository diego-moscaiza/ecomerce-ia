interface Props {
    id: string;
}

export const getPrendasById = async ({ id }) => {
    const rest = await fetch(`https://${id}`);
    const prendas = rest.json;
    return prendas;
}

export const getAllPrendas = async () => {
    try {
        const res = await fetch(`https://`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                query: {},
                options: {
                },
            }),
        });
        const jsonData = await res.json();
        return jsonData;

    } catch (error) {
        throw new Error("Error al obtener los datos");
    }
}
