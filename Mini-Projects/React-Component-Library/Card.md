
### Card.js

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './Card.css'; // You can style it as needed

const Card = ({ title, children, footer }) => {
  return (
    <div className="card">
      {title && <div className="card-header">{title}</div>}
      <div className="card-body">{children}</div>
      {footer && <div className="card-footer">{footer}</div>}
    </div>
  );
};

// Define prop types for type safety
Card.propTypes = {
  title: PropTypes.string,
  children: PropTypes.node.isRequired,
  footer: PropTypes.node,
};

export default Card;
```

### Card.css (Basic Styling)

```css
/* Card basic styles */
.card {
  border: 1px solid #ddd;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  width: 300px;
  margin: 20px;
}

.card-header {
  background-color: #f7f7f7;
  padding: 16px;
  font-size: 18px;
  font-weight: bold;
  border-bottom: 1px solid #ddd;
  border-radius: 8px 8px 0 0;
}

.card-body {
  padding: 16px;
  font-size: 16px;
}

.card-footer {
  background-color: #f7f7f7;
  padding: 12px;
  border-top: 1px solid #ddd;
  font-size: 14px;
  text-align: center;
  border-radius: 0 0 8px 8px;
}
```

### Usage Example:

You can import and use the `Card` component in your app like this:

```jsx
import React from 'react';
import Card from './Card';

const App = () => {
  return (
    <div>
      <Card title="Card Title" footer="Card Footer">
        <p>This is the content inside the card.</p>
      </Card>
      
      <Card title="Another Card">
        <p>This card doesn't have a footer, but it has content!</p>
      </Card>
    </div>
  );
};

export default App;
```

### Key Features:
- **Props**:
  - `title`: The title that appears at the top of the card (optional).
  - `children`: The content inside the card. This is a required prop.
  - `footer`: The footer content that appears at the bottom of the card (optional).
  
- **Styling**: The card has basic styles (border, padding, and shadow) that you can customize in the `Card.css` file. It supports optional `title` and `footer` sections.

This is a basic `Card` component, and you can further customize it with more features like images, buttons, or additional content sections. Let me know if you'd like to adjust anything! 😊
