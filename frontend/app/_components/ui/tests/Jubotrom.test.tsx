import { render, screen } from "@testing-library/react";
import { Jubotrom } from "../Jubotrom";

describe("Jubotrom", () => {

    it("renderiza o componente como uma tag section e possui os articles internos", () => {
        render(<Jubotrom/>);
        expect(screen.getByRole("region", { name: "hero" })).toBeInTheDocument();
        const articles = screen.getAllByRole("article");
        expect(articles.length).toBe(2);
        expect(articles[0]).toHaveAttribute("id", "hero-text-article");
        expect(articles[1]).toHaveAttribute("id", "hero-image-article");
    });

    it("renderiza o texto do hero corretamente", () => {
        render(<Jubotrom/>);
        const articles = screen.getAllByRole("article");
        const heroTextArticle = articles[0];
        expect(heroTextArticle).toBeInTheDocument();
        expect(heroTextArticle).toHaveTextContent("Tenha tesão ao aplicar...");
        expect(heroTextArticle).toHaveTextContent("e facilidade ao revisar suas vagas");
    });

    it("renderiza a grade de pontos de maneira fixa com parallax", () => {
        render(<Jubotrom/>);
        const section = screen.getByRole("region", { name: "hero" });
        const backgroundDiv = section.querySelector("div");
        expect(backgroundDiv).toBeInTheDocument();
        expect(backgroundDiv).toHaveStyle("background-attachment: fixed");
        expect(backgroundDiv).toHaveStyle("background-image: radial-gradient(circle, rgba(0,0,0,0.15) 1px, transparent 1px)");
    });
});