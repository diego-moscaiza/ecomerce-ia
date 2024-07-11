export type Response = {
    productos : Usuario[];
}

export type Usuario = {
    first_name:   string;
    last_name:    string;
    username:     string;
    email:        string;
}