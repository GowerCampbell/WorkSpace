
### Input.js

```jsx
import React from 'react';
import PropTypes from 'prop-types';
import './Input.css'; // You can style it as needed

const Input = ({ type, value, onChange, placeholder, disabled, size }) => {
  return (
    <div className={`input-container ${size}`}>
      <input
        type={type}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        disabled={disabled}
        className="input-field"
      />
    </div>
  );
};

// Define default props
Input.defaultProps = {
  type: 'text',
  value: '',
  placeholder: 'Enter value',
  disabled: false,
  size: 'medium',
};

// Define prop types for type safety
Input.propTypes = {
  type: PropTypes.string,
  value: PropTypes.string,
  onChange: PropTypes.func.isRequired,
  placeholder: PropTypes.string,
  disabled: PropTypes.bool,
  size: PropTypes.oneOf(['small', 'medium', 'large']),
};

export default Input;
```

### Input.css (Basic Styling)

```css
/* Basic input styles */
.input-container {
  margin-bottom: 15px;
}

.input-field {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  outline: none;
  transition: border-color 0.3s ease;
}

.input-field:focus {
  border-color: #007bff;
}

.input-field:disabled {
  background-color: #f0f0f0;
  cursor: not-allowed;
}

/* Sizes */
.input-container.small .input-field {
  font-size: 14px;
  padding: 8px;
}

.input-container.medium .input-field {
  font-size: 16px;
  padding: 10px;
}

.input-container.large .input-field {
  font-size: 18px;
  padding: 12px;
}
```

### Usage Example:

You can import and use the `Input` component in your app like this:

```jsx
import React, { useState } from 'react';
import Input from './Input';

const App = () => {
  const [textValue, setTextValue] = useState('');
  const [emailValue, setEmailValue] = useState('');

  const handleTextChange = (e) => setTextValue(e.target.value);
  const handleEmailChange = (e) => setEmailValue(e.target.value);

  return (
    <div>
      <h1>React Input Component</h1>
      <Input 
        type="text"
        value={textValue}
        onChange={handleTextChange}
        placeholder="Enter your name"
        size="medium"
      />
      <Input 
        type="email"
        value={emailValue}
        onChange={handleEmailChange}
        placeholder="Enter your email"
        size="large"
      />
      <Input 
        type="text"
        value=""
        onChange={() => {}}
        placeholder="Disabled Input"
        disabled
        size="small"
      />
    </div>
  );
};

export default App;
```

### Key Features:
- **Props**:
  - `type`: The input type (e.g., `'text'`, `'email'`, `'password'`).
  - `value`: The current value of the input field.
  - `onChange`: A function that is called when the input value changes (to update the value).
  - `placeholder`: The placeholder text for the input field.
  - `disabled`: A boolean to control whether the input is disabled.
  - `size`: Defines the size of the input (`'small'`, `'medium'`, `'large'`).

- **Styling**:
  - The input has different sizes that can be applied by setting the `size` prop. The `input-field` class changes based on the size, modifying the padding and font size.
  - The `focus` state of the input changes the border color to highlight the input field when it's focused.
  - The input field has a simple disabled style (lighter background and non-interactive).

### How it Works:
- The `Input` component accepts various props like `type`, `value`, `onChange`, and `size`, which you can customize based on the needs of your app.
- The `onChange` handler allows you to update the state when the input changes, and the `value` prop binds the input to that state.
- The `disabled` prop disables the input, preventing interaction.

This is a basic input component, and you can extend it further to support other features like validation, icons, or custom error messages. Let me know if you'd like to expand on it! 😊
