"use client";

import { NavBar } from "./_components/ui/NavBar";
import { Jubotrom } from "./_components/ui/Jubotrom";
export default function HomePage() {
  return(
    <>
      <NavBar/>
      <main>
        <Jubotrom/>
        <section className="min-h-screen p-20 bg-black/80"></section>
      </main>
    </>
  
  );  
} 