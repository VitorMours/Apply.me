import { render, screen } from "@testing-library/react";
import AuthLoginPage from "../page";

jest.mock("next/navigation", () => ({
  useRouter: () => ({
    push: jest.fn(),
    replace: jest.fn(),
    back: jest.fn(),
    forward: jest.fn(),
    refresh: jest.fn(),
    prefetch: jest.fn(),
  }),
  usePathname: () => "/auth/login",
  useSearchParams: () => new URLSearchParams(),
}));

describe("AuthLoginPage", () => {
    it("should render the login page with the form and the Navbar", () => {
        render(<AuthLoginPage />);

        expect(screen.getByRole("navigation")).toBeInTheDocument();
        expect(screen.getByRole("form")).toBeInTheDocument();

        expect(screen.getByLabelText(/email/i)).toBeInTheDocument();
        expect(screen.getByLabelText(/senha/i)).toBeInTheDocument();
        expect(screen.getByRole("button", { name: /login/i })).toBeInTheDocument();
    })
});

describe("AuthLoginPageForm", () => {
    it("should have the correct input types and placeholders", () => {
        render(<AuthLoginPage />);

        const emailInput = screen.getByLabelText(/email/i);
        const passwordInput = screen.getByLabelText(/senha/i);

        expect(emailInput).toHaveAttribute("type", "email");
        expect(passwordInput).toHaveAttribute("type", "password");

        expect(emailInput).toHaveAttribute("placeholder", "nome@exemplo.com");
        expect(passwordInput).toHaveAttribute("placeholder", "password");
    });
});
