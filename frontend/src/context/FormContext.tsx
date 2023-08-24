import React, { createContext, useContext, useState, ReactNode } from 'react';

interface FormContextType {
  formSubmitted: boolean;
  setFormSubmitted: React.Dispatch<React.SetStateAction<boolean>>;
}

const FormContext = createContext<FormContextType | undefined>(undefined);

export const FormProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [formSubmitted, setFormSubmitted] = useState(false);

  return (
    <FormContext.Provider value={{ formSubmitted, setFormSubmitted }}>
      {children}
    </FormContext.Provider>
  );
};

export const useForm = (): FormContextType => {
  const context = useContext(FormContext);
  if (!context) {
    throw new Error('useForm must be used within a FormProvider');
  }
  return context;
};
