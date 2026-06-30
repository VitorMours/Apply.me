'use client'
import { useState } from "react";
import AuthService, { LoginUserDTO } from "@/lib/services/authService";
import { NavBar } from "@/app/_components/ui/NavBar";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { toast } from "sonner";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/navigation";
import { Spinner } from "@/components/ui/spinner";
import { ApiError } from "@/lib/errors";

const messages: Record<number, string> = {
  400: "Problema no envio dos dados.",
  401: "Erro nas credenciais de login.",
  404: "Destino nao encontrado.",
  405: "Envio de formulario em formato indisponivel.",
  422: "Problema no processamento do formulario.",
  500: "Erro no servidr."
};

export default function AuthLoginPage() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const router = useRouter();

  async function handleSubmit(event: React.SubmitEvent<HTMLFormElement>) {
    event.preventDefault();
    setLoading(true);

    const formData = new FormData(event.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;

    const payload: LoginUserDTO = { email, password };

    try {
      const response = await AuthService.login(payload);
      setLoading(false);
      router.push('/dashboard');
    } catch (error) {

      if (error instanceof ApiError) {
        const message = messages[error.status] ?? "Erro desconhecido";
        toast.error("Erro durante o login", { position: "bottom-right", description: message });
      } else {
        toast.error("Erro durante o login", { position: "bottom-right", description: "Erro desconhecido" });
      }
      console.trace(`Error: ${error}`)
    } finally {
      setLoading(false);
    }
  }

  return (
    <>
      <NavBar />
      <main className="min-h-screen w-full flex items-center justify-center px-4 py-10">

        <Card className="w-full max-w-md rounded-lg shadow-md">
          <CardHeader className="space-y-1">
            <CardTitle className="text-2xl text-center">Login</CardTitle>
          </CardHeader>
          <CardContent>
            <form className="space-y-4" onSubmit={handleSubmit}>
              <div className="space-y-2">
                <Label htmlFor="email">Email</Label>
                <Input className="rounded-lg" name="email" id="email" type="email" placeholder="nome@exemplo.com" required />
              </div>

              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <Label htmlFor="password">Senha</Label>
                  <a href="/forget-password" className="text-sm text-primary hover:underline underline-offset-4">
                    Esqueceu a senha?
                  </a>
                </div>
                <Input className="rounded-lg" name="password" id="password" type="password" placeholder="password" required />
              </div>

              {loading ? <Spinner className="w-full" /> : <Button type="submit" className="w-full rounded-lg">Entrar</Button>}
            </form>
          </CardContent>
        </Card>
      </main>
    </>
  );
}