"use client";

export function Jubotrom() {
  return (
    <section aria-label="hero" className="relative flex flex-col w-full min-h-screen overflow-hidden">
      <div
        className="absolute inset-0 -z-10"
        style={{
          backgroundImage:
            "radial-gradient(circle, rgba(0,0,0,0.15) 1px, transparent 1px)",
          backgroundSize: "24px 24px",
          backgroundAttachment: "fixed",
        }}
      />

      <article id="hero-text-article" className="p-20 flex flex-col gap-5 justify-center w-1/2 min-h-screen relative z-10">
        <h1 className="text-8xl font-bold">Tenha tesão ao aplicar...</h1>
        <p className="text-2xl italic font-light">e facilidade ao revisar suas vagas</p>
      </article>
      <article id="hero-image-article" className="relative z-10"></article>
    </section>
  );
}