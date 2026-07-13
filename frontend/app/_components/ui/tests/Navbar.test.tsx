import { render, screen } from "@testing-library/react";
import { NavBar } from "../NavBar";

describe("NavBar", () => {
  it("renderiza o componente com a tag nav", () => {
    render(<NavBar />);
    expect(screen.getByRole("navigation")).toBeInTheDocument();
  });

  it("renderiza o link da logo/home", () => {
    render(<NavBar />);
    const homeLink = screen.getByRole("link", { name: /apply/i });
    expect(homeLink).toBeInTheDocument();
    expect(homeLink).toHaveAttribute("href", "/");
  });

  it("renderiza o link de login apontando para /auth/login", () => {
    render(<NavBar />);
    const loginLink = screen.getByRole("link", { name: /login/i });
    expect(loginLink).toBeInTheDocument();
    expect(loginLink).toHaveAttribute("href", "/auth/login");
  });

  it("renderiza o link de sign up apontando para /auth/signup", () => {
    render(<NavBar />);
    const signupLink = screen.getByRole("link", { name: /sign up/i });
    expect(signupLink).toBeInTheDocument();
    expect(signupLink).toHaveAttribute("href", "/auth/signup");
  });
});