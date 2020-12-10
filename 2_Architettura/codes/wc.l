%{
    unsigned charCount = 0;
    unsigned wordCount = 0;
    unsigned lineCount = 0;
%}

%option noyywrap

word [^ \t\n]+
eol \n

%%

{word}  {
    wordCount++;
    charCount += yyleng;
}

{eol}   {
    charCount++;
    lineCount++;
}

.       {
    charCount++;
}

%%

int main()
{
    yylex();
    printf("%i %i %i\n", lineCount, wordCount, charCount);
}