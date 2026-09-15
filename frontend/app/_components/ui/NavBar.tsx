"use client";

import Link from "next/link";
import { Button } from "@/components/ui/button"; // Importe o componente Button do Shadcn

export function NavBar() { 
    return (
        <nav className="w-full border-b bg-background/80 backdrop-blur-sm sticky top-0 z-50 px-6 py-4 flex items-center justify-between">
            <div className="font-bold text-xl tracking-tight">
                <Link href="/">Apply</Link>
            </div>
            
            <div className="flex items-center gap-4">
                <Button className="rounded-md" variant="outline" asChild>
                    <Link href="/auth/login">
                        Login
                    </Link>
                </Button>
                <Button className="rounded-md" asChild>
                    <Link href="/auth/signup">
                        Sign up
                    </Link>
                </Button>
            </div>
        </nav>
    );
}