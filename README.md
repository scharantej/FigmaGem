## Application Design for Gemini Figma Extension

### HTML Files

- **index.html**: The main HTML file, responsible for displaying the chat interface and providing options for interacting with Gemini.
- **chat.html**: A partial HTML file that includes the chat conversation history and input field. This allows for easy updates to the chat without reloading the entire page.

### Routes

**Main Route:**

- **`/`**: This route renders the `index.html` file and serves as the entry point of the application.

**Chat Routes:**

- **`/send_message`**: Handles POST requests to send a message to Gemini.
- **`/get_messages`**: Handles GET requests to fetch the latest messages from Gemini.

**Other Routes:**

- **`/refresh_figma`**: Handles GET requests to refresh the Figma file within the extension.
- **`/apply_changes`**: Handles POST requests to apply changes made in Figma back to the design file.