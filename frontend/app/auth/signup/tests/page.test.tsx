import { render, screen } from "@testing-library/react"
import AuthSignupPage from "../page";


describe("AuthSignupPage", () => {
    it("should render the signup page with the form and the Navbar", () => {
        render(<AuthSignupPage />);

        expect(screen.getByRole("navigation")).toBeInTheDocument();
        expect(screen.getByRole("form")).toBeInTheDocument();
    });

});