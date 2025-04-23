-- Update category names to replace / with or
UPDATE categories 
SET name = 'Salary or Wages'
WHERE name = 'Salary/Wages';

UPDATE categories 
SET name = 'Bonuses or Commissions'
WHERE name = 'Bonuses/Commissions';

UPDATE categories 
SET name = 'Pension or Retirement Funds'
WHERE name = 'Pension/Retirement Funds';

-- Update category names to replace & with and
UPDATE categories 
SET name = 'Food and Groceries'
WHERE name = 'Food & Groceries';

UPDATE categories 
SET name = 'Personal and Household'
WHERE name = 'Personal & Household';

UPDATE categories 
SET name = 'Entertainment and Leisure'
WHERE name = 'Entertainment & Leisure';

UPDATE categories 
SET name = 'Debt and Financial Obligations'
WHERE name = 'Debt & Financial Obligations';

UPDATE categories 
SET name = 'Savings and Investments'
WHERE name = 'Savings & Investments'; 