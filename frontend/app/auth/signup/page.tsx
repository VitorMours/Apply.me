import { NavBar } from "@/app/_components/ui/NavBar";
import { Card, CardContent, CardHeader } from "@/components/ui/card";
import { CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Button } from "@/components/ui/button";

export default function AuthSignupPage() {
  return (
    <>
        <NavBar/>  
        <main className="min-h-screen w-full flex items-center justify-center px-4 py-10">
            <Card className="w-full max-w-md  rounded-lg shadow-md">
              <CardHeader className="flex items-center justify-center">
                <CardTitle className="text-xl">Inscrever-se</CardTitle>
              </CardHeader>
              <CardContent className="space-y-4">
                
                <div className="flex items-center justify-between">
                  <div>
                    <Label className="mb-2 ml-1 text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70" htmlFor="nome">Nome</Label>
                    <Input className="rounded-md" id="nome" type="text" placeholder="Digite seu nome" />
                  </div>
                  <div>
                    <Label className="mb-2 ml-1 text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70" htmlFor="sobrenome">Sobrenome</Label>
                    <Input className="rounded-md" id="sobrenome" type="text" placeholder="Digite seu sobrenome" />
                  </div>
                </div>

                <div>
                  <Label className="mb-2 ml-1 text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70" htmlFor="email">Email</Label>
                  <Input className="rounded-md" id="email" type="email" placeholder="Digite seu email" />
                </div>

                <div>
                  <Label className="mb-2 ml-1 text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70" htmlFor="password">Senha</Label>
                  <Input className="rounded-md" id="password" type="password" placeholder="Digite sua senha" />
                </div>
                <Button className="w-full rounded-md">Entrar</Button>
              </CardContent>
            </Card>
          </main>
    </>
  );
}