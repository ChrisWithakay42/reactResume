import { test, expect } from "@playwright/test";

test('submitting contact form', async ({ page }) => {
  await page.goto('http://localhost:3000');

  // Fill out the form
  await page.fill('input[name="name"]', 'John Doe');
  await page.fill('input[name="phone"]', '1234567890');
  await page.fill('input[name="email"]', 'test@example.com');
  await page.fill('input[name="subject"]', 'Testing');
  await page.fill('textarea[name="message"]', 'This is a test message.');

  // Submit the form
  await page.click('button[type="submit"]');

  // Wait for the form to reset
  await page.waitForFunction(() => {
    return (
      (document.querySelector('input[name="name"]') as HTMLInputElement).value === '' &&
      (document.querySelector('input[name="phone"]') as HTMLInputElement).value === '' &&
      (document.querySelector('input[name="email"]') as HTMLInputElement).value === '' &&
      (document.querySelector('input[name="subject"]') as HTMLInputElement).value === '' &&
      (document.querySelector('textarea[name="message"]') as HTMLTextAreaElement).value === ''
    );
  });

  // Assert for success message
  const successMessage = await page.textContent('.success-message'); // Replace with your actual selector
  expect(successMessage).toContain('Email sent successfully');
});
