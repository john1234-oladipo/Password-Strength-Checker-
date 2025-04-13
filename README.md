# Password Strength Checker 🔒

A web-based and command-line tool that evaluates password strength and provides actionable feedback to help users create more secure passwords.

## Features ✨

- **Real-time strength evaluation** with visual feedback
- **Comprehensive checks** for:
  - Minimum length (8+ characters)
  - Uppercase and lowercase letters
  - Numbers and special characters
  - Common/predictable patterns
  - Repeated characters
- **Color-coded strength meter** (red → orange → green)
- **Detailed improvement suggestions**
- **Command-line version** available for developers

## Technologies Used 🛠️

- **Web Version**:
  - HTML5, CSS3, JavaScript (Vanilla JS)
  - Responsive design

- **CLI Version**:
  - Python 3.x
  - `getpass` module for secure input
  - Regular expressions for pattern matching

## Installation ⚙️

### Web Version
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-strength-checker.git
   ```
2. Open `index.html` in your browser

### Command-Line Version
1. Ensure you have Python 3 installed
2. Run the script:
   ```bash
   python password_strength.py
   ```

## Usage 🚀

### Web Interface
1. Type your password in the input field
2. View real-time strength feedback
3. Follow suggestions to improve your password

### Command-Line
```bash
$ python password_strength.py
Password Strength Checker
Enter your password for analysis (input will be hidden):

Password Strength: Strong (4/5)

Suggestions to improve your password:
- Add special characters
```

## Future Enhancements 🔮

- [ ] Password entropy calculation
- [ ] Integration with "Have I Been Pwned" API
- [ ] Password generation feature
- [ ] Browser extension version
- [ ] Multi-language support

## Contributing 🤝

Contributions are welcome! Please follow these steps:
1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments 🏆

- Inspired by modern password security best practices
- Thanks to all open-source contributors who made this possible

---

**Happy (and secure) coding!** 💻🔐
