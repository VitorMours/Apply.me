'use client'
import { useState } from "react";
import AuthService, { LoginUserDTO } from "@/lib/services/authService";
import { NavBar } from "@/app/_components/ui/NavBar";
import { Card, CardHeader, CardTitle, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";
import { useRouter } from "next/navigation";
import { Spinner } from "@/components/ui/spinner";



export default function AuthLoginPage() {
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function handleSubmit(event: React.SubmitEvent<HTMLFormElement>){
    event.preventDefault();  
    setLoading(true);

    const formData = new FormData(event.currentTarget);
    const email = formData.get("email") as string;
    const password = formData.get("password") as string;

    const payload: LoginUserDTO = { email, password };
    try{
      
      await AuthService.login(payload);
      setLoading(false);
      router.push('/dashboard');
    }catch(error){
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
                <Input className="rounded-lg" id="email" type="email" placeholder="nome@exemplo.com" required />
              </div>
              
              <div className="space-y-2">
                <div className="flex items-center justify-between">
                  <Label htmlFor="password">Senha</Label>
                  <a href="/forget-password" className="text-sm text-primary hover:underline underline-offset-4">
                    Esqueceu a senha?
                  </a>
                </div>
                <Input className="rounded-lg" id="password" type="password" placeholder="password" required />
              </div>
              
              {loading ? <Spinner className="w-full"/> : <Button type="submit" className="w-full rounded-lg">Entrar</Button>} 
            </form>
          </CardContent>
        </Card>
      </main>
    </>
  );
}