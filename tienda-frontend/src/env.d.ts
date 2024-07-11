/// <reference types="astro/client" />

declare namespace App {
    interface Locals {
        first_name: string;
        last_name: string;
        username: string;
        email: string;
        is_logged : boolean;
    }
}
