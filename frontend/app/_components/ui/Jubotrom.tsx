"use client";

export function Jubotrom() {
  return (
    <section className="relative w-full h-screen overflow-hidden">
      {/* Texto — precisa de z-10 pra ficar acima da grade */}
      <div className="relative z-10 flex flex-col w-1/2 h-screen justify-center p-10 items-start">
        <h1 className="text-6xl font-bold text-left">
          Tenha Tesão, <br /> em aplicar para vagas
        </h1>
        <p className="text-2xl font-light italic text-left">
          Encontre a vaga perfeita, a um deslize de tela
        </p>
      </div>

      {/* Grade — só na metade direita, atrás do texto */}
      <div
        className="absolute top-0 right-0 w-1/2 h-screen
          bg-[radial-gradient(rgba(255,255,255,0.15)_1px,transparent_1px)]
          bg-[size:20px_20px]"
      />
    </section>
  );
}