### Button.js

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './Button.css'; // You can style it as needed

const Button = ({ onClick, label, color, size, disabled }) => {
  return (
    <button
      onClick={onClick}
      className={`btn ${color} ${size} ${disabled ? 'disabled' : ''}`}
      disabled={disabled}
    >
      {label}
    </button>
  );
};

// Define default props
Button.defaultProps = {
  label: 'Click Me',
  color: 'primary', // default color
  size: 'medium', // default size
  disabled: false,
};

// Define prop types for type safety
Button.propTypes = {
  onClick: PropTypes.func.isRequired,
  label: PropTypes.string,
  color: PropTypes.oneOf(['primary', 'secondary', 'danger']),
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  disabled: PropTypes.bool,
};

export default Button;
```

### Button.css (Basic Styling)

```css
/* Button basic styles */
.btn {
  padding: 10px 20px;
  border: none;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s;
}

.btn.primary {
  background-color: #007bff;
  color: white;
}

.btn.secondary {
  background-color: #6c757d;
  color: white;
}

.btn.danger {
  background-color: #dc3545;
  color: white;
}

.btn.small {
  font-size: 14px;
  padding: 6px 12px;
}

.btn.medium {
  font-size: 16px;
  padding: 10px 20px;
}

.btn.large {
  font-size: 18px;
  padding: 12px 24px;
}

.btn:disabled,
.btn.disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
```

### Usage Example:

You can import and use this `Button` component in your app like this:

```jsx
import React from 'react';
import Button from './Button';

const App = () => {
  const handleClick = () => {
    alert('Button clicked!');
  };

  return (
    <div>
      <Button onClick={handleClick} label="Primary Button" color="primary" size="medium" />
      <Button onClick={handleClick} label="Secondary Button" color="secondary" size="large" />
      <Button onClick={handleClick} label="Danger Button" color="danger" size="small" />
      <Button onClick={handleClick} label="Disabled Button" color="primary" size="medium" disabled />
    </div>
  );
};

export default App;
```

### Key Features:
- **Props**:
  - `onClick`: Function to execute when the button is clicked.
  - `label`: The text that appears on the button.
  - `color`: Sets the button color (options: `'primary'`, `'secondary'`, `'danger'`).
  - `size`: Defines the size of the button (options: `'small'`, `'medium'`, `'large'`).
  - `disabled`: If true, disables the button.
  
- **Styling**: The button has basic styles that you can customize further via the `Button.css` file. The class names adjust according to the color and size props.
